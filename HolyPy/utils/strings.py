#!/usr/bin/python2
# coding: utf-8

from holypy.utils.maths import ceil_modulus

################################################################################
### Methods
################################################################################

def pad(string, char, chunk, ljust = True):
    if ljust:
        return string.ljust(ceil_modulus(len(string), chunk), char)
    else:
        return string.rjust(ceil_modulus(len(string), chunk), char)

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
