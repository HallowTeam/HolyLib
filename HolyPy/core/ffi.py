#!/usr/bin/python2
# coding: utf-8

import ctypes
import ctypes.util

################################################################################
### Methodes
################################################################################

def cimport(fn):
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    if isinstance(fn, str):
        return getattr(libc, fn)
    return [getattr(libc, x) for x in fn]

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
