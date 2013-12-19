#!/usr/bin/python2
# coding: utf-8

from holypy.crypto.xor    import xor
from holypy.utils.iters   import split

################################################################################
### Constants
################################################################################
"""
iv = Init    Vector: vecteur initialisateur
dv = Decoded Value : valeur  intermediaire
ev = Encoded Value : valeur  encode
"""

CBC_ERROR = "Padding Error"

################################################################################
### Decryption Class
################################################################################

class CBCIterDecrypt():
    def __init__(self, cipher, size):
        self.dvs    = []
        self.size   = size
        self.blocks = split(cipher, self.size)

    def __iter__(self):
        self.dv  = []
        self.dvs = []
        self.reset()
        return self

    def clear(self):
        self.count = 0xFF

    def reset(self):
        self.count = -1

    def next(self):
        self.count += 1
        if self.count > 0xFF:
            raise StopIteration
        return self.next_iv()

    def next_iv(self):
        """
        Generation du prochain IV
        """
        iv = chr(self.count)
        for key in self.dv:
            iv += chr(key ^ (len(self.dv) + 1))
        iv = iv.rjust(self.size, chr(0))
        return iv + self.blocks[-1 - len(self.dvs)]

    def success(self):
        """
        Validation du dernier IV
        """
        self.dv.insert(0, self.count ^ (len(self.dv) + 1))
        if len(self.dv) == self.size:
            self.dvs.insert(0, self.dv)
            self.dv = []
        if len(self.dvs) + 1 >= len(self.blocks):
            self.clear()
        else:
            self.reset()

    def decrypt(self):
        """
        Dechiffrement du message
        """
        plain = ""
        for i, dv in enumerate(self.dvs):
            plain += decrypt(self.blocks[i], dv)
        return plain

################################################################################
### Encryption Class
################################################################################

class CBCIterEncrypt():
    def __init__(self, plain, size, iv = None, dv = None):
        self.iv     = iv
        self.dvs    = []
        self.clue   = dv
        self.size   = size
        self.chunks = split(pad(plain, self.size), self.size)

    def __iter__(self):
        self.dv    = []
        self.dvs   = []
        self.block = ""
        self.reset()
        if self.iv == None:
            self.iv    = chr(0) * self.size
            self.block = self.iv
        elif self.clue != None:
            self.prepend(self.clue)
        else:
            self.block = self.iv
        return self

    def prepend(self, dv):
        self.dvs.insert(0, dv)
        if len(self.dvs) >= len(self.chunks):
            self.clear()
            return
        self.block = encrypt(self.chunks[-len(self.dvs)], dv)
        self.dv    = []

    def clear(self):
        self.count = 0xFF

    def reset(self):
        self.count = -1

    def next(self):
        self.count += 1
        if self.count > 0xFF:
            raise StopIteration
        return self.next_iv()

    def next_iv(self):
        """
        Generation du prochain IV
        """
        iv = chr(self.count)
        for key in self.dv:
            iv += chr(key ^ (len(self.dv) + 1))
        iv = iv.rjust(self.size, chr(0))
        return iv + self.block

    def success(self):
        """
        Validation du dernier IV
        """
        self.dv.insert(0, self.count ^ (len(self.dv) + 1))
        self.reset()
        if len(self.dv) == self.size:
            self.prepend(self.dv)

    def encrypt(self):
        """
        Chiffrement du message
        """
        cipher = ""
        for i, dv in enumerate(self.dvs):
            cipher += encrypt(self.chunks[i], dv)
        return cipher + self.iv

################################################################################
### Methods
################################################################################

def decrypt(iv, dv):
    """
    Dechiffrement de @iv avec @dv
    """
    plain = ""
    iv    = iv
    for i, key in enumerate(dv):
        plain += xor(iv[i], key)
    return plain

def encrypt(plain, dv):
    """
    Chiffrement de @plain avec @dv
    """
    iv = ""
    for i, key in enumerate(dv):
        iv += xor(plain[i], key)
    return iv

def pad(plain, size):
    """
    Ajout du padding
    """
    offset = size - (len(plain) % size)
    return plain + chr(offset) * offset

def unpad(plain):
    """
    Suppression du padding
    """
    return plain[:-ord(plain[-1])]

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
