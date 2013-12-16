#!/usr/bin/python2
# coding: utf-8

import sys
import pexpect

################################################################################
### Methods
################################################################################

def ssh(cmd, passwd, pattern):
    """
    Ouvre une session ssh avec pexpect
    """
    process = spawn(cmd)
    if process.expect(["password:", pattern]) == 0:
        sendline(passwd, process)
        process.expect(pattern)
    return process

def spawn(cmd):
    """
    Lance une commande avec pexpect
    """
    process = pexpect.spawn(cmd)
    process.logfile = sys.stdout
    return process

def interact(process):
    """
    Active le mode interaction pour une commande pexpect
    """
    process.logfile = None
    process.interact()

def sendline(line, process, EOF = True):
    """
    Envoye une ligne a une commande pexpect
    """
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
