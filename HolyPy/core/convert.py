#!/usr/bin/python2
# coding: utf-8

from holypy.core.iter import split

################################################################################
### Methods
################################################################################

def itos(i, ltr = True):
    """int to string"""
    s = ""
    while i != 0:
        s += chr(i & 0xff)
        i  = (i >> 8)
    return s[::-1] if ltr else s

def stoi(s, ltr = False):
    """string to int"""
    i = 0
    for c in s[::-1] if ltr else s:
        i <<= 8
        i  += ord(c)
    return i

def btos(b):
    """bytes to string"""
    return "".join([c[2:].decode("hex") for c in split(b, 4)])

def stob(s):
    """string to bytes"""
    return "".join(["\\x%02x" % ord(c) for c in s])

################################################################################
### Module
################################################################################

if __name__ == '__main__':
  pass
