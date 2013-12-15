#!/usr/bin/python2
# coding: utf-8

import string

################################################################################
### Constants
################################################################################

CHARSET = string.uppercase

################################################################################
### Methods
################################################################################

def format_key(key):
    """Format <key> into a valid key"""
    return [c for c in key.upper() if c in CHARSET]

def format_text(text):
    """Format <text> into a valid text"""
    return text.upper()

def encrypt(plain, key):
    """Encrypt data with Vigenere algorithm"""
    key    = format_key(key)
    count  = 0
    plain  = format_text(plain)
    cipher = ""
    for c in plain:
        if c in CHARSET:
            index   = CHARSET.index(c)
            offset  = CHARSET.index(key[count % len(key)])
            cipher += CHARSET[(index + offset) % len(CHARSET)]
            count  += 1
        else:
            cipher += c
    return cipher

def decrypt(cipher, key):
    """Decrypt data with Vigenere algorithm"""
    key    = format_key(key)
    count  = 0
    plain  = ""
    cipher = format_text(cipher)
    for c in cipher:
        if c in CHARSET:
            index   = CHARSET.index(c)
            offset  = CHARSET.index(key[count % len(key)])
            plain  += CHARSET[(index - offset) % len(CHARSET)]
            count  += 1
        else:
            plain  += c
    return plain

def revert(cipher, plain):
    """Find key with plaintext attack"""
    key    = ""
    plain  = format_key(plain)
    cipher = format_key(cipher)
    for a, b in zip(cipher, plain):
        if a in CHARSET:
            index   = CHARSET.index(a)
            offset  = CHARSET.index(b)
            key    += CHARSET[(index - offset) % len(CHARSET)]
    return key

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
