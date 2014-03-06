#!/usr/bin/python2
# coding: utf-8

from string             import uppercase
from holypy.core.string import alphacharset, alphaindex
from holypy.core.iter   import getitem

################################################################################
### Methods
################################################################################

def caesar(cipher, offset = None):
    """Decalle les lettres de @offset ou brute force"""

    ############################################################################
    ############################################################################

    def _caesar(cipher, offset):
        """Decalle les lettres de @offset"""
        plain = ""
        for c in cipher:
            if c.isalpha():
                plain += getitem(alphacharset(c), alphaindex(c) + offset)
            else:
                plain += c
        return plain

    ############################################################################
    ############################################################################

    if offset == None:
        return [_caesar(cipher, i) for i in xrange(len(uppercase))]
    else:
        return _caesar(cipher, offset)

def translate(cipher, charset, offset = None):
    """Decalle les caracteres de @offset ou brute force"""

    ############################################################################
    ############################################################################

    def _translate(cipher, charset, offset):
        """Decalle les caracteres de @offset"""
        plain = ""
        for c in cipher:
            if c in charset:
                plain += getitem(charset, charset.index(c) + offset)
            else:
                plain += c
        return plain

    ############################################################################
    ############################################################################

    if offset == None:
        return [_translate(cipher, charset, i) for i in xrange(len(charset))]
    else:
        return _translate(cipher, charset, offset)

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
