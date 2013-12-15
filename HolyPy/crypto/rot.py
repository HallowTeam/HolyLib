#!/usr/bin/python2
# coding: utf-8

import string

################################################################################
### Methods
################################################################################

def rot(cipher, offset = None):
    """Translate all chars of cipher"""
    if offset == None:
        results = []
        for i in xrange(1, 256):
            results += [rot_trans(cipher, i)]
        return results
    else:
        return rot_trans(cipher, offset)

def rot_trans(cipher, offset):
    """Translate all chars of cipher"""
    return "".join([chr((ord(c) + offset) % 256) for c in cipher])

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
