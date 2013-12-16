#!/usr/bin/python2
# coding: utf-8

import string

################################################################################
### Methods
################################################################################

def rot(cipher, offset = None):
    """
    Decalle chaque caractere de @cipher de @offset
    Si @offset n'est pas renseigne, @offset prendra toutes les valeurs possible
    """
    if offset == None:
        results = []
        for i in xrange(1, 256):
            results += [rot_trans(cipher, i)]
        return results
    else:
        return rot_trans(cipher, offset)

def rot_trans(cipher, offset):
    """
    Decalle chaque caractere de @cipher de @offset
    """
    return "".join([chr((ord(c) + offset) % 256) for c in cipher])

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
