#!/usr/bin/python2
# coding: utf-8
# Source: https://wiki.python.org/moin/BitManipulation

import struct

################################################################################
### Bits Methods
################################################################################

def set_bit(value, offset):
    """
    Active le bit a l'index @offset
    """
    return value | (1 << offset)

def test_bit(value, offset):
    """
    Retourne 0 si le bit a l'index @offset n'est pas active
    """
    return value & (1 << offset)

def clear_bit(value, offset):
    """
    Desactive le bit a l'index @offset
    """
    return value & ~(1 << offset)

def toggle_bit(value, offset):
    """
    Modifie le bit a l'index @offset
    """
    return value ^ (1 << offset)

################################################################################
### Size Methods
################################################################################

def byte(value):
    return value & 0xff

def word(value):
    return value & 0xffff

def dword(value):
    return value & 0xffffffff

def qword(value):
    return value & 0xffffffffffffffff

################################################################################
### Methods
################################################################################

def endian(value, size = "I"):
    return struct.unpack(">" + size, struct.pack("<" + size, value))[0]

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
