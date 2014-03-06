#!/usr/bin/python2
# coding: utf-8

import sys
import pexpect

################################################################################
### Constantes
################################################################################

PROMPT = "\$ "

################################################################################
### Methodes generales
################################################################################

def spawn(cmd):
    """Execute une commande"""
    process         = pexpect.spawn(cmd)
    process.logfile = sys.stdout
    return process

def output(cmd):
    """Execute une commande et retourne son output"""
    process         = pexpect.spawn(cmd)
    process.logfile = None
    process.expect(pexpect.EOF)
    return process.before

def expect(process, pattern = PROMPT):
    """Attente d'un pattern"""
    process.expect(pattern)

def sendline(process, line, EOL = True):
    """Envoie de donnees"""
    logfile         = process.logfile
    process.logfile = None
    if EOL:
        process.sendline("".join(map(lambda x: "\x16" + x, line)))
    else:
        process.send("".join(map(lambda x: "\x16" + x, line)))
    process.logfile = logfile

def interact(process):
    """Activation du mode interaction"""
    if process.logfile in [sys.stdout, sys.stderr]:
        process.logfile = None
    process.interact()

################################################################################
### Methodes ssh
################################################################################

def ssh(cmd, passwd, pattern = PROMPT):
    """Ouvre une session ssh"""
    process = spawn(cmd)
    if process.expect(["password:", pattern]) == 0:
        sendline(process, passwd)
        expect(process, pattern)
    return process

def sshconf(process, pattern = PROMPT):
    commands = (
        'alias ls="ls --color=auto"',
        'alias ll="ls --color=auto -l"',
        'alias la="ls --color=auto -la"',
        'alias  l="ls --color=auto -l"',
        'alias ..="cd .."',
        'alias up="cd .."',
    )
    for command in commands:
        sendline(process, command)
        expect(process, pattern)

def sshinteract(process, conf = True, pattern = PROMPT):
    if conf:
        sshconf(process, pattern)
    interact(process)

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
