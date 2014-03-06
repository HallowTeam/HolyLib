#!/usr/bin/python2
# coding: utf-8

from __future__         import absolute_import
from string             import lowercase, uppercase
from holypy.core.math   import rceil

################################################################################
### Methodes
################################################################################

def pad(string, c, chunksize, ltr):
    """Complete @string afin d'atteindre une taille multiple de @size"""
    if ltr:
        return string.ljust(rceil(len(string), chunksize), c)
    else:
        return string.rjust(rceil(len(string), chunksize), c)

def lpad(string, c, chunksize): return pad(string, c, chunksize, True)
def rpad(string, c, chunksize): return pad(string, c, chunksize, False)

def alphacharset(c):
    """Retourne l'alphabet de la lettre @c"""
    return lowercase if c.islower() else uppercase

def alphaindex(c):
    """Retourne l'index de la lettre @c dans l'alphabet"""
    return alphacharset(c).index(c)

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
