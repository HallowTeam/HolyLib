#!/usr/bin/python2
# coding: utf-8

from holypy.utils.iters import split

################################################################################
### Methods
################################################################################

def string_to_bytes(string):
    return "".join(map(lambda x: "\\x%02x" % (ord(x)), string))

def bytes_to_string(bytes_):
    return "".join(map(lambda x: chr(int(x[2:4], 16)), split(bytes_, 4)))

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
