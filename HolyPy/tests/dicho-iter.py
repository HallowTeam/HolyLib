#!/usr/bin/python2
# coding: utf-8

import string

from holypy.crypto.dicho import *

passwd = "b_0n_j0ur _ ! l3s 4mis !!! C0c0r1c4!!!!!!!"
dicho  = DichoIter(MODE_LTE, charset = set(string.printable))

i = 0
for text in dicho:
    print i, text

    i += 1
    if i == -1:
        break

    if passwd == text:
        dicho.eq(True)
    elif passwd <= text:
        dicho.lte()
    elif passwd > text:
        dicho.gt()

print "[+] Plain:", dicho.text
