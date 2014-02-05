#!/usr/bin/python2
# coding: utf-8

import string

from holypy.crypto.dicho import DichoIter

passwd = "b0nj0ur l3s 4mis !!!"
dicho  = DichoIter(charset = string.printable)

for text in dicho:
    print text
    if passwd == text:
        dicho.eq()
        break
    elif passwd >= text:
        dicho.gte()
    else:
        dicho.lt()
print "[+]", text
