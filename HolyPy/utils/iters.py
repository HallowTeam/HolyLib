#!/usr/bin/python2
# coding: utf-8

################################################################################
### Methods
################################################################################

def split(iter_, size = 2):
    """Split <iter_> every <size> members"""
    return [iter_[i:i + size] for i in xrange(0, len(iter_), size)]

def iterize(obj, type_ = None):
    """Return <obj> if it's iterable or an iterable object containing <obj>"""
    if type_ == None:
        if isinstance(obj, list) or isinstance(obj, tuple):
            return obj
        return [obj]
    elif type_ == list:
        if isinstance(obj, list):
            return obj
        else:
            return [obj]
    elif type_ == tuple:
        if isinstance(obj, tuple):
            return obj
        else:
            return (obj)

################################################################################
### Module
################################################################################

if __name__ == '__main__':
  pass
