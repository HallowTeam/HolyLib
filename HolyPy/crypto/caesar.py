#!/usr/bin/python2
# coding: utf-8

import string

################################################################################
### Methods
################################################################################

def caesar(cipher, offset = None):
    """Apply caesar algorithm to the cipher"""
    if offset == None:
        results = []
        for i in xrange(1, len(string.lowercase)):
            results += [caesar_trans(cipher, i)]
        return results
    else:
        return caesar_trans(cipher, offset)

def caesar_trans(cipher, offset):
    """Apply caesar algorithm to the cipher"""
    text = ""
    for c in cipher:
        if c.islower():
            text += string.lowercase[(string.lowercase.index(c) + offset) % len(string.lowercase)]
        elif c.isupper():
            text += string.uppercase[(string.uppercase.index(c) + offset) % len(string.uppercase)]
        else:
            text += c
    return text

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
