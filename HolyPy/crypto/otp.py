#!/usr/bin/python2
# coding: utf-8

import string

################################################################################
### Methods
################################################################################

def encrypt(plaintext, key, charset = string.uppercase):
    """
    Chiffre @plaintext avec l'algorithme OTP
    """
    ciphertext = ""
    for c1, c2 in zip(plaintext, key):
        i1 = charset.index(c1)
        i2 = charset.index(c2)
        ciphertext += charset[(i1 + i2) % len(charset)]
    return ciphertext

def decrypt(ciphertext, key, charset = string.uppercase):
    """
    Dechiffre @ciphertext avec l'algorithme OTP
    """
    plaintext = ""
    for c1, c2 in zip(ciphertext, key):
        i1 = charset.index(c1)
        i2 = charset.index(c2)
        plaintext += charset[(i1 - i2) % len(charset)]
    return plaintext

################################################################################
################################################################################
################################################################################

if __name__ == '__main__':
    pass
