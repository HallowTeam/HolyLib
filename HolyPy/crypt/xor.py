#!/usr/bin/python2
# coding: utf-8

import string

from math               import ceil
from holypy.core.iter   import split, getitem
from holypy.core.memory import xor
from holypy.core.output import *

################################################################################
### Constantes
################################################################################

KEYSET  = set(string.letters + string.digits + "_")
TEXTSET = set(string.letters + string.digits + "_ ',.!")

################################################################################
### Class
################################################################################

class Xor(object):
    def __init__(self, cipher, keyset = KEYSET, textset = TEXTSET):
        self.errno   = 0
        self.cipher  = cipher
        self.keyset  = keyset
        self.textset = textset

    def analyze(self, keylen, filters = None):
        """
        Analyze du xor pour une clef de longueur @keylen

        @filters = dict[index]{
            "charset": [], # Charset autorise pour l'index
            "exclude": [], # Lettres non autorise pour l'index
        }
        """
        self.errno   = -1
        self.keylen  = keylen
        self.chunks  = split(self.cipher, self.keylen)
        self.charset = set()
        self.ignores = set()
        self.matches = [{} for i in xrange(self.keylen)]
        for i in xrange(self.keylen):
            for k in self.keyset:
                if not self.skip(i, k, filters):
                    match   = False
                    chars   = []
                    charset = set()
                    for chunk in self.chunks:
                        if i >= len(chunk):
                            break
                        c = xor(chunk[i], k)
                        if not c in self.textset:
                            match         = False
                            self.ignores |= set(c)
                            break
                        match    = True
                        charset |= set(c)
                        chars.append(c)
                    if match:
                        self.charset      |= charset
                        self.matches[i][k] = {
                            "chars"   : chars,
                            "charset" : charset,
                        }
            if len(self.matches[i]) == 0:
                self.errno = i
                break

    def analyze_plain(self, plain, start = 0):
        """Devine une partie de la clef grace @plain"""
        i     = start
        key   = []
        index = 0
        while i < len(self.cipher):
            success  = False
            matchset = getitem(self.matches, i)
            for k, data in matchset.items():
                char = xor(self.cipher[i], k)
                if char == plain[index]:
                    key.append(k)
                    success = True
                    index  += 1
                    break
            if success == False:
                i    -= index
                index = 0
                key   = []
            elif len(key) == len(plain):
                break
            i += 1
        offset = i % self.keylen - len(key)
        for x in xrange(len(key)):
            offset += 1
            offset  = offset if offset >= 0 else self.keylen + offset
            offset  = offset % self.keylen
            print "[%02d]" % offset, fmt("['%c']" % key[x], WHITE),
        print
        if i != len(self.cipher):
            self.analyze_plain(plain, i + 1)

    def analyze_length(self, limit = 30, filters = None):
        """Trouve toutes les longueur de clef possibles"""
        for i in xrange(1, min(limit, len(self.cipher))):
            self.analyze(i, filters)
            if self.errno == -1:
                print "%02d" % i,
                self.report_key()

    def skip(self, i, k, filters):
        if not filters or not i in filters.keys():
            return False
        if "charset" in filters[i].keys():
            return not k in filters[i]["charset"]
        if "exclude" in filters[i].keys():
            return k in filters[i]["exclude"]

    def report(self):
        """Affiche un bilan de la derniere analyze"""
        self.report_status()
        print
        self.report_charset()
        print
        self.report_key()
        print
        self.report_keyset()

    def report_status(self):
        """Affiche le statut de la derniere analyze"""
        if self.errno != -1:
            print fmt("[-] Xor: failure at index %d" % self.errno, RED)
        else:
            print fmt("[+] Xor: success", GREEN)

    def report_charset(self):
        """Affiche les differentes charset"""
        print fmt("[charset]", MAGENTA)
        print fmt(sorted([x for x in self.charset]), WHITE)
        print
        print fmt("[ignores]", MAGENTA)
        print fmt(sorted([x for x in self.ignores]), WHITE)

    def report_key(self):
        """Affiche la clef"""
        key = ""
        for matchset in self.matches:
            if len(matchset) == 0:
                continue
            if len(matchset) == 1:
                k, data = matchset.items()[0]
                key += fmt(k, BLUE)
            else:
                key += fmt("?", WHITE)
        print "[*] %s" % key

    def report_keyset(self):
        """Affiche les caracteres possible pour la clef"""
        for i, matchset in enumerate(self.matches):
            if len(matchset) == 1:
                print "[%02d]" % i, fmt(sorted([k for k, data in matchset.items()]), BLUE)
            elif len(matchset) != 0:
                print "[%02d]" % i, fmt(sorted([k for k, data in matchset.items()]), WHITE)
            else:
                print "[%02d]" % i, fmt("[X]", RED)

    def report_index(self, index):
        """Affiche des information sur @index"""
        i = 0
        for k, data in self.matches[index].items():
            if i != 0:
                print
            print fmt("['%c': charset - chars]" % k, MAGENTA)
            print fmt(sorted([x for x in data["charset"]]), WHITE)
            print fmt(data["chars"], WHITE)
            i = 1

    def report_plain(self):
        """Affiche le plaintext"""
        plain   = ""
        guesses = [[] for i in xrange(self.keylen)]
        for i, matchset in enumerate(self.matches):
            charslen   = int(ceil(len(self.cipher) / float(self.keylen)))
            guesses[i] = [[-1, False] for x in xrange(charslen)]
            if len(matchset) == 0:
                continue
            for k, data in matchset.items():
                for x, c in enumerate(data["chars"]):
                    if guesses[i][x][0] == None:
                        break
                    elif guesses[i][x][0] == -1:
                        guesses[i][x][0] = c
                    elif guesses[i][x][0] != c:
                        if guesses[i][x][0].lower() == c.lower():
                            guesses[i][x][1] = True
                        else:
                            guesses[i][x][0] = None
        for i in xrange(self.keylen):
            for data in guesses:
                if i < len(data):
                    char = data[i][0]
                    case = data[i][1]
                    if char == -1:
                        plain += fmt("X", MAGENTA)
                    elif char == None:
                        plain += fmt("?", WHITE)
                    elif case == False:
                        plain += fmt(char, BLUE)
                    else:
                        plain += fmt(char, YELLOW)
        print "[*] %s" % plain

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
