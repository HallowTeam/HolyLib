#!/usr/bin/python2
# coding: utf-8

from holypy.crypto.xor    import xor
from holypy.utils.iters   import split
from holypy.utils.convert import hex_to_string

################################################################################
### Constants
################################################################################

CBC_ERROR = "Padding Error"

################################################################################
### Methods
################################################################################

class CBCIterator():
    def __init__(self, size, cipher):
        self.iv      = []
        self.ivs     = []
        self.size    = size * 2
        self.count   = -1
        self.blocks  = split(cipher, self.size)

    def __iter__(self):
        self.iv    = []
        self.ivs   = []
        self.count = -1
        return self

    def next(self):
        self.count += 1
        if self.count > 0xFF:
            raise StopIteration
        return self.next_iv()

    def next_iv(self):
        """
        Generation du prochain IV
        """
        iv  = ""
        for byte in self.iv[::-1]:
            iv += "%02X" % (byte ^ (len(self.iv) + 1))
        iv  = "%02X" % (self.count) + iv
        iv  = iv.rjust(self.size, "0")
        iv += self.blocks[::-1][len(self.ivs)]
        return iv

    def success(self):
        """
        Validation du dernier IV
        """
        self.iv.append(self.count ^ (len(self.iv) + 1))
        if len(self.iv) == self.size / 2:
            self.ivs.append(self.iv)
            self.iv = []
        self.count = -1
        if len(self.ivs) + 1 >= len(self.blocks):
            self.count = 0xFF

    def decrypt(self):
        """
        Decryptage du message
        """
        plain = ""
        for i, iv in enumerate(self.ivs[::-1]):
            plain += decrypt(self.blocks[i], iv)
        return plain

def decrypt(cipher, values):
    """
    Decryptage de @cipher avec @values
    """
    plain  = ""
    cipher = hex_to_string(cipher)
    for i, value in enumerate(values[::-1]):
        plain += xor(cipher[i], value)
    return plain

# def encrypt(plain, size, values):
#     offset = size - (len(plain) % size)
#     plain  = plain + chr(offset) * offset

################################################################################
### Module
################################################################################


if __name__ == '__main__':
    pass
