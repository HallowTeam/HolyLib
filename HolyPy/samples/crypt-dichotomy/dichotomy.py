#!/usr/bin/python2
# coding: utf-8

import string
import random

from holypy.crypt.dichotomy import *

def brute():
    passwd = ''.join(random.choice(string.printable) for _ in range(50))
    def fn(vector, abort):
        if abort:
            return
            if len(vector) == len(passwd):
                return RET_EQ
            if passwd == vector:
                return RET_EQ
        else:
            if passwd >= vector:
                return RET_GTE
            elif passwd < vector:
                return RET_LT

    breaker = Dichotomy(fn, charset = set(string.printable))
    breaker.run()

    print "'%s'" % breaker.text.encode("hex")
    print "'%s'" % passwd.encode("hex")

    return breaker.text == passwd

brute()
