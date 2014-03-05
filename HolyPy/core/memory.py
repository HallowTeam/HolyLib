#!/usr/bin/python2
# coding: utf-8
# Source: https://wiki.python.org/moin/BitManipulation

import struct

################################################################################
### Constantes
################################################################################

BIT   = 1
BYTE  = 8
WORD  = 16
DWORD = 32
QWORD = 64

SIZE_REPR = {
    BYTE  : "B",
    WORD  : "H",
    DWORD : "I",
    QWORD : "Q",
}

################################################################################
### Methodes masques
################################################################################

def mask(n, size):
    """Creation d'un masque de @n * @size bits"""
    return (1 << (n * size)) - 1

def zmask(n, size, off, offsize):
    """Creation d'un masque de @n * @size bits a partir de @off * @offsize bits"""
    return mask(n, size) << (off * offsize)

def czmask(val, off, offsize):
    """Creation d'un masque de valeur @val a partir de @off * @offsize bits"""
    return val << (off * offsize)

def rmask(mask):
    """Creation du masque inverse de @mask"""
    return ~mask

def masku(n): return mask(n, BIT)
def maskb(n): return mask(n, BYTE)
def maskw(n): return mask(n, WORD)
def maskd(n): return mask(n, DWORD)
def maskq(n): return mask(n, QWORD)

def zmasku(n, off): return zmask(n, BIT  , off, BIT)
def zmaskb(n, off): return zmask(n, BYTE , off, BYTE)
def zmaskw(n, off): return zmask(n, WORD , off, WORD)
def zmaskd(n, off): return zmask(n, DWORD, off, DWORD)
def zmaskq(n, off): return zmask(n, QWORD, off, QWORD)

def czmasku(val, off): return czmask(val, off, BIT)
def czmaskb(val, off): return czmask(val, off, BYTE)
def czmaskw(val, off): return czmask(val, off, WORD)
def czmaskd(val, off): return czmask(val, off, DWORD)
def czmaskq(val, off): return czmask(val, off, QWORD)

################################################################################
### Methodes tailles
################################################################################

def fit(val, size):
    """Retourne @value sur @size bits"""
    return val & mask(size, BIT)

def fitu(val): return fit(val, BIT)
def fitb(val): return fit(val, BYTE)
def fitw(val): return fit(val, WORD)
def fitd(val): return fit(val, DWORD)
def fitq(val): return fit(val, QWORD)

################################################################################
### Methodes setters/getters bits
################################################################################

def getb(value, offset):
    """Retourne le bit a l'index @offset"""
    return value & (1 << offset)

def setb(value, offset):
    """Active le bit a l'index @offset"""
    return value | (1 << offset)

def flipb(value, offset):
    """Change le bit a l'index @offset"""
    return value ^ (1 << offset)

def unsetb(value, offset):
    """Desactive le bit a l'index @offset"""
    return value & ~(1 << offset)

################################################################################
### Methodes setters/getters generiques
################################################################################

def zget(val, n, size, off, offsize):
    """Retourne les donnees correspondantes au masque (@n, @size, @off, @offsize)"""
    return (val & zmask(n, size, off, offsize)) >> (off * offsize)

def zset(val, x, n, size, off, offsize):
    """Remplace les donnees correspondantes au masque (@n, @size, @off, @offsize)"""
    return (val & rmask(zmask(n, size, off, offsize))) | czmask(fit(x, n * size), off, offsize)

def zgetu(val, n, off): return zget(val, n, BIT  , off, BIT)
def zgetb(val, n, off): return zget(val, n, BYTE , off, BYTE)
def zgetw(val, n, off): return zget(val, n, WORD , off, WORD)
def zgetd(val, n, off): return zget(val, n, DWORD, off, DWORD)
def zgetq(val, n, off): return zget(val, n, QWORD, off, QWORD)

def zsetu(val, x, n, off): return zset(val, x, n, BIT  , off, BIT)
def zsetb(val, x, n, off): return zset(val, x, n, BYTE , off, BYTE)
def zsetw(val, x, n, off): return zset(val, x, n, WORD , off, WORD)
def zsetd(val, x, n, off): return zset(val, x, n, DWORD, off, DWORD)
def zsetq(val, x, n, off): return zset(val, x, n, QWORD, off, QWORD)

################################################################################
### Methodes endian
################################################################################

def endian(val, size = DWORD):
    """Modifie l'endian de @val"""
    if isinstance(size, int):
        size = SIZE_REPR[size]
    return struct.unpack("<" + size, struct.pack(">" + size, val))[0]

def endianu(value): return endian(fitu(value), BYTE)
def endianb(value): return endian(fitb(value), BYTE)
def endianw(value): return endian(fitw(value), WORD)
def endiand(value): return endian(fitd(value), DWORD)
def endianq(value): return endian(fitq(value), QWORD)

################################################################################
### Methodes operateurs
################################################################################

def shr(val, size, off = 1, bit = False):
    """
    Decalle les bits de @val (taille @size) de @off vers la droite
    @val est ensuite complete avec des 0 (bit = True) ou 1 (bit = False)
    """
    return fit((fit(val, size) >> off) | (zmasku(off, size - off) if bit else 0), size)

def shl(val, size, off = 1, bit = False):
    """
    Decalle les bits de @val (taille @size) de @off vers la gauche
    @val est ensuite complete avec des 0 (bit = True) ou 1 (bit = False)
    """
    return fit((fit(val, size) << off) | (masku(off) if bit else 0), size)

def ror(val, size, off = 1):
    """Fonction asm ror"""
    return fit(zsetu(fit(val, size) >> off, zgetu(val, off, 0), off, size - off), size)

def rol(val, size, off = 1):
    """Fonction asm rol"""
    return fit(zsetu(fit(val, size) << off, zgetu(val, off, size - off), off, 0), size)

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
