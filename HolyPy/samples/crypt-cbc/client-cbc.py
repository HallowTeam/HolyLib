#!/usr/bin/python2
# coding: utf-8

import subprocess

from holypy.crypt.cbc import *

def fn(vector):
    print vector
    try:
        process = subprocess.check_output(['./server-cbc.py', '-d', vector], stderr = subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

# ENCODE
plain   = "Crazy !"
plain   = "Crazy ! You Are !"
breaker = CBCEncrypt(plain, 8, fn)
if not breaker.run():
    print "[-] CODED"
    exit(1)

print "[+] CODED:", breaker.encrypt()

# DECODE
breaker = CBCDecrypt(breaker.encrypt(), 8, fn)
if not breaker.run():
    print "[-] PLAIN"
    exit(1)

print "[+] PLAIN:", breaker.decrypt()

# ENCODE WITH OBJECT
plain   = "Happy !"
plain   = "Happy ! I Am !"
breaker = CBCEncrypt(plain, 8, fn, obj = breaker)
if not breaker.run():
    print "[-] CODED"
    exit(1)

print "[+] CODED:", breaker.encrypt()

# DECODE
breaker = CBCDecrypt(breaker.encrypt(), 8, fn)
if not breaker.run():
    print "[-] PLAIN"
    exit(1)

print "[+] PLAIN:", breaker.decrypt()
