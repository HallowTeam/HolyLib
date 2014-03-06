#!/usr/bin/python2
# coding: utf-8

from string             import lowercase, uppercase
from holypy.core.iter   import getitem

################################################################################
### Methods
################################################################################

def translate(cipher, offset = None):
    """Decalle les lettres de @offset caractere ou brute force"""

    ############################################################################
    ############################################################################

    def _translate(cipher, offset):
        """Decalle les lettres de @offset"""
        plain = ""
        for c in cipher:
            if c.islower():
                plain += getitem(lowercase, lowercase.index(c) + offset)
            elif c.isupper():
                plain += getitem(uppercase, uppercase.index(c) + offset)
            else:
                plain += c
        return plain

    ############################################################################
    ############################################################################

    if offset == None:
        return [_translate(cipher, i) for i in xrange(len(lowercase))]
    else:
        return _translate(cipher, offset)

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
