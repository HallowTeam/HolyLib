#!/usr/bin/python2
# coding: utf-8

################################################################################
### Methodes
################################################################################

def read_until(fd, c = chr(0), eof = True):
    """Lis les donnees jusqu'a rencontrer @c ou eof"""
    data = ""
    while True:
        char = fd.read(1)
        if not char or char == c:
            if not char and not eof:
                raise EOFError()
            break
        data += char
    return data

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
