#!/usr/bin/python2
# coding: utf-8

from holypy.core.string import alphacharset, alphaindex
from holypy.core.iter   import getitem

################################################################################
### Methods
################################################################################

def encrypt(plain, key):
    """Chiffrement"""
    count  = 0
    cipher = ""
    for c in plain:
        if c.isalpha():
            offset  = alphaindex(getitem(key, count))
            cipher += getitem(alphacharset(c), alphaindex(c) + offset)
            count  += 1
        else:
            cipher += c
    return cipher

def decrypt(cipher, key):
    """Dechiffrement"""
    count = 0
    plain = ""
    for c in cipher:
        if c.isalpha():
            offset = alphaindex(getitem(key, count))
            plain += getitem(alphacharset(c), alphaindex(c) - offset)
            count += 1
        else:
            plain += c
    return plain

def analyze(cipher, plain):
    """Cherche la clef a partir de @plain"""
    key = ""
    for a, b in zip(cipher, plain):
        if a.isalpha():
            key += getitem(alphacharset(a), alphaindex(a) - alphaindex(b))
    return key

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
