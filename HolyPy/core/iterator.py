#!/usr/bin/python2
# coding: utf-8

################################################################################
### Methodes
################################################################################

def split(it, size = 2):
    """Decoupe @it en blocks de @size membres"""
    return [it[i:i + size] for i in xrange(0, len(it), size)]

def mindex(it):
    """Retourne l'index du milieu de @it ou -1"""
    return -1 if len(it) == 0 else ((len(it) - 1) / 2)

def iterize(obj):
    """Converti @obj en une liste si necessaire"""
    if not isinstance(obj, list):
        obj = [obj]
    return obj

################################################################################
### Module
################################################################################

if __name__ == '__main__':
  pass
