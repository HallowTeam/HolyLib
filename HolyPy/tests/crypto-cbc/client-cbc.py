#!/usr/bin/python2
# coding: utf-8

import re
import subprocess
from   holypy.crypto.cbc       import *
from   holypy.utils.iters      import split
from   holypy.binaries.phelper import *

if __name__ == '__main__':
    # ENCODE
    plain  = "Crazy !"
    cbc    = CBCIterEncrypt(plain, 8)
    for i in cbc:
        try:
            process = subprocess.check_output(['./server-cbc.py', '-d', i.encode("hex")], stderr = subprocess.PIPE)
            cbc.success()
        except subprocess.CalledProcessError:
            pass
    cipher = cbc.encrypt().encode("hex")
    print "[+] CODED:", cipher

    # DECODE
    cbc    = CBCIterDecrypt(cipher.decode("hex"), 8)
    for i in cbc:
        try:
            process = subprocess.check_output(['./server-cbc.py', '-d', i.encode("hex")], stderr = subprocess.PIPE)
            cbc.success()
        except subprocess.CalledProcessError:
            pass
    print "[+] PLAIN:", cbc.decrypt()

    # ENCODE
    plain  = "Happy !"
    cbc    = CBCIterEncrypt(plain, 8, iv = cbc.blocks[-1], dv = cbc.dvs[-1])
    for i in cbc:
        try:
            process = subprocess.check_output(['./server-cbc.py', '-d', i.encode("hex")], stderr = subprocess.PIPE)
            cbc.success()
        except subprocess.CalledProcessError:
            pass
    cipher = cbc.encrypt().encode("hex")
    print "[+] CODED:", cipher

    # DECODE
    cbc    = CBCIterDecrypt(cipher.decode("hex"), 8)
    for i in cbc:
        try:
            process = subprocess.check_output(['./server-cbc.py', '-d', i.encode("hex")], stderr = subprocess.PIPE)
            cbc.success()
        except subprocess.CalledProcessError:
            pass
    print "[+] PLAIN:", cbc.decrypt()
