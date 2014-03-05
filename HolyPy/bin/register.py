#!/usr/bin/python2
# coding: utf-8

from holypy.core.memory import zgetb, zgetw, zgetd, zgetq
from holypy.core.memory import zsetb, zsetw, zsetd, zsetq

################################################################################
### Classe ZRegister
################################################################################
# Pour Ufox, l'homme qui fait trembler les kernels !

class ZRegister(object):
    @property
    def zl(self): return zgetb(self._val, 1, 0)

    @property
    def zh(self): return zgetb(self._val, 1, 1)

    @property
    def zx(self): return zgetw(self._val, 1, 0)

    @property
    def ezx(self): return zgetd(self._val, 1, 0)

    @property
    def rzx(self): return zgetq(self._val, 1, 0)

    @zl.setter
    def zl(self, val): self._val = zsetb(self._val, val, 1, 0)

    @zh.setter
    def zh(self, val): self._val = zsetb(self._val, val, 1, 1)

    @zx.setter
    def zx(self, val): self._val = zsetw(self._val, val, 1, 0)

    @ezx.setter
    def ezx(self, val): self._val = zsetd(self._val, val, 1, 0)

    @rzx.setter
    def rzx(self, val): self._val = zsetq(self._val, val, 1, 0)

    def __init__(self, val):
        self._val = val

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
