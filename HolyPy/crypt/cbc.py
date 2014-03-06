#!/usr/bin/python2
# coding: utf-8

"""
iv = Init    Vector: vecteur initialisateur
dv = Decoded Value : valeur  intermediaire
ev = Encoded Value : valeur  encode
"""

from holypy.core.memory import xor
from holypy.core.iter   import split

################################################################################
### Classe de chiffrement
################################################################################

class CBCEncrypt(object):
    def __init__(self, plain, size, fn, iv = None, dv = None, obj = None):
        self.iv     = iv
        self.fn     = fn
        self.dv     = []
        self.dvs    = []
        self.obj    = obj
        self.clue   = dv
        self.size   = size
        self.plain  = plain
        self.chunk  = ""
        self.chunks = split(pad(plain, self.size), self.size)

    def init(self):
        if self.obj:
            self.iv   = self.obj.chunks[-1].encode("hex")
            self.clue = self.obj.dvs[-1]
        if self.iv == None:
            self.iv    = chr(0) * self.size
            self.chunk = self.iv
            return
        self.iv = self.iv.decode("hex")
        if self.clue != None:
            self.prepend(self.clue)
        else:
            self.chunk = self.iv

    def run(self):
        """Chiffrement du message"""
        self.init()
        self.count = -1
        if len(self.dvs) >= len(self.chunks):
            return True
        while self.next():
            if self.fn(self.vector()):
                if self.success():
                    return True
        return False

    def next(self):
        """Incrementation du vecteur"""
        self.count += 1
        if self.count > 0xff:
            return False
        return True

    def vector(self):
        """Generation du vecteur"""
        vector  = chr(self.count)
        for key in self.dv:
            vector += chr(key ^ (len(self.dv) + 1))
        vector  = vector.rjust(self.size, chr(0))
        vector += self.chunk
        return vector.encode("hex")

    def success(self):
        """Validation du vecteur"""
        self.dv.insert(0, self.count ^ (len(self.dv) + 1))
        if len(self.dv) == self.size:
            return self.prepend(self.dv)
        self.count = -1
        return False

    def prepend(self, dv):
        self.dvs.insert(0, dv)
        if len(self.dvs) >= len(self.chunks):
            return True
        self.chunk = self.encrypt_iv(self.chunks[-len(self.dvs)], dv)
        self.dv    = []
        return False

    def encrypt(self):
        """Chiffrement du plain"""
        cipher = ""
        for i, dv in enumerate(self.dvs):
            cipher += self.encrypt_iv(self.chunks[i], dv)
        return (cipher + self.iv).encode("hex")

    def encrypt_iv(self, plain, dv):
        """Chiffrement de @plain"""
        iv = ""
        for i, key in enumerate(dv):
            iv += xor(plain[i], key)
        return iv

################################################################################
### Classe de dechiffrement
################################################################################

class CBCDecrypt(object):
    def __init__(self, cipher, size, fn):
        self.fn     = fn
        self.dv     = []
        self.dvs    = []
        self.size   = size
        self.cipher = cipher
        self.chunks = split(self.cipher.decode("hex"), self.size)

    def run(self):
        """Dechiffrement du message"""
        self.count = -1
        while self.next():
            if self.fn(self.vector()):
                if self.success():
                    return True
        return False

    def next(self):
        """Incrementation du vecteur"""
        self.count += 1
        if self.count > 0xff:
            return False
        return True

    def vector(self):
        """Generation du vecteur"""
        vector  = chr(self.count)
        for key in self.dv:
            vector += chr(key ^ (len(self.dv) + 1))
        vector  = vector.rjust(self.size, chr(0))
        vector += self.chunks[-1 - len(self.dvs)]
        return vector.encode("hex")

    def success(self):
        """Validation du vecteur"""
        self.dv.insert(0, self.count ^ (len(self.dv) + 1))
        if len(self.dv) == self.size:
            self.dvs.insert(0, self.dv)
            self.dv = []
        if len(self.dvs) + 1 >= len(self.chunks):
            return True
        self.count = -1
        return False

    def decrypt(self):
        """Dechiffrement du cipher"""
        plain = ""
        for i, dv in enumerate(self.dvs):
            plain += self.decrypt_iv(self.chunks[i], dv)
        return unpad(plain)

    def decrypt_iv(self, iv, dv):
        """Dechiffrement d'un iv"""
        plain = ""
        for i, key in enumerate(dv):
            plain += xor(iv[i], key)
        return plain

################################################################################
### Methodes
################################################################################

def pad(plain, size):
    """Complete @plain afin d'atteindre une longueur de @size"""
    offset = size - (len(plain) % size)
    return plain + chr(offset) * offset

def unpad(plain):
    """Supprimer le padding de @plain"""
    return plain[:-ord(plain[-1])]

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
