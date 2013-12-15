#!/usr/bin/python2
# coding: utf-8

import sys
import pexpect

################################################################################
### Methods
################################################################################

def ssh(cmd, passwd, pattern):
    process = spawn(cmd)
    if process.expect(["password:", pattern]) == 0:
        sendline(passwd, process)
        process.expect(pattern)
    return process

def spawn(cmd):
    process = pexpect.spawn(cmd)
    process.logfile = sys.stdout
    return process

def interact(process):
    process.logfile = None
    process.interact()

def sendline(line, process, EOF = True):
    process.logfile = None
    if EOF:
        process.sendline("".join(map(lambda x: "\x16" + x, line)))
    else:
        process.send("".join(map(lambda x: "\x16" + x, line)))
    process.logfile = sys.stdout

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
