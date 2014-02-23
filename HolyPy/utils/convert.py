#!/usr/bin/python2
# coding: utf-8

import string
from   holypy.utils.iters import split

################################################################################
### Methods
################################################################################

def string_with_bytes(string_):
    """
    Remplace tous les characters speciaux par leur equivalent \\x??
    """
    encoded = ""
    for c in string_:
        if c in set(string.printable) - set(string.whitespace) | set(" "):
            encoded += c
        # elif c == "\n":
        #     encoded += "\\n"
        # elif c == "\r":
        #     encoded += "\\r"
        # elif c == "\t":
        #     encoded += "\\t"
        else:
            encoded += "\\x%02X" % ord(c)
    print encoded

def string_to_bytes(string_):
    """
    Remplace chaque caractere de @string_ par sont equivalent \\x??
    """
    return "".join(map(lambda x: "\\x%02x" % (ord(x)), string_))

def bytes_to_string(bytes_):
    """
    Remplace chaque \\x?? de @bytes_ par sont equivalent ascii
    """
    return "".join(map(lambda x: chr(int(x[2:4], 16)), split(bytes_, 4)))

def int_to_string(int_):
    """
    Convertion d'un entier en chaine de caractere
    """
    string = ""
    for byte in split(hex(int_)[2:].strip("L")):
        string += chr(int(byte, 16))
    return string

def string_to_int(str_):
    """
    Convertion d'une chaine de caractere en entier
    """
    value = 0
    for i, c in enumerate(str_):
        value <<= 8
        value  += ord(c)
    return value

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
