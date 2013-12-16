#!/usr/bin/python2
# coding: utf-8

import string
from   holypy.utils.iters     import split
from   holypy.utils.prettify  import *

################################################################################
### Constants
################################################################################

KEY_CHARSET  = set(string.printable) - set(string.whitespace) - set("!\"#$%&'()*+,-./:;<=>?@[\\]^`{|}~")
TEXT_CHARSET = set(string.printable) - set("\"#$%&*+/<=>@[\\]^`|~")

################################################################################
### Methods
################################################################################

def xor(plain, key):
    """
    Xor @plain et @key
    """
    if isinstance(key, int):
        return chr(ord(plain[0]) ^ key)
    cipher = ""
    for i, c in enumerate(plain):
        cipher += chr(ord(c) ^ ord(key[i % len(key)]))
    return cipher

def brute(cipher, key_len, key_charset = KEY_CHARSET, text_charset = TEXT_CHARSET, verbose = True):
    """
    Effectue une attaque brute force sur @cipher
    """
    chunks  = split(cipher, key_len)
    matches = []
    charset = set()
    success = False
    for i in xrange(key_len):
        ignored = set()
        for c in key_charset:
            chars   = set()
            success = True
            for chunk in chunks:
                if i < len(chunk):
                    char = xor(chunk[i], c)
                    if not char in text_charset:
                        ignored |= set(char)
                        success  = False
                        break
                    chars |= set(char)
                else:
                    continue
            if success:
                if i == len(matches):
                    matches.append([])
                matches[i].append(c)
                charset |= set(chars)
        if i >= len(matches):
            break
    else:
        success = True
        ignored = []
    if verbose:
        debug(success, matches, sorted(charset), sorted(ignored))
    return success, matches, sorted(charset), sorted(ignored)

def debug(success, matches, charset, ignored):
    """
    Affiche les informations retournee par une attaque brute force
    """
    passwd = ""
    for chars in matches:
        if len(chars) == 1:
            passwd += prettify(chars[0], BLUE, attributes = BOLD)
        else:
            passwd += prettify("?", WHITE, attributes = BOLD)
    if success == True:
        print prettify("[+] Success", GREEN, attributes = BOLD)
        print prettify("[+] Matches:", GREEN, attributes = BOLD), passwd
        print prettify(matches, YELLOW, attributes = BOLD)
        print prettify("[+] Charset:", GREEN, attributes = BOLD), charset
    else:
        print prettify("[-] Failure at index %d" % len(matches), RED, attributes = BOLD)
        print prettify("[-] Matches:", RED, attributes = BOLD), passwd
        print matches
        print prettify("[-] Charset:", RED, attributes = BOLD), charset
        print prettify("[-] Ignored:", RED, attributes = BOLD), prettify(ignored, YELLOW, attributes = BOLD)

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
