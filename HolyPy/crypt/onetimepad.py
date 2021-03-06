#!/usr/bin/python2
# coding: utf-8

from string             import uppercase
from holypy.core.iter   import getitem

################################################################################
### Methods
################################################################################

def encrypt(plain, key, charset = uppercase):
    """Chiffrement"""
    cipher = ""
    for c1, c2 in zip(plain, key):
        if c1 in charset:
            i1      = charset.index(c1)
            i2      = charset.index(c2)
            cipher += getitem(charset, i1 + i2)
        else:
            cipher += c1
    return cipher

def decrypt(cipher, key, charset = uppercase):
    """Dechiffrement"""
    plain = ""
    for c1, c2 in zip(cipher, key):
        if c1 in charset:
            i1     = charset.index(c1)
            i2     = charset.index(c2)
            plain += getitem(charset, i1 - i2)
        else:
            plain += c1
    return plain

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
