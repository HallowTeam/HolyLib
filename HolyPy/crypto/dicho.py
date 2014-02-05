#!/usr/bin/python2
# coding: utf-8

import string

from holypy.utils.iters import middle

################################################################################
### Constants
################################################################################

CHARSET  = list(string.letters + string.digits)
MODE_GTE = "MODE_GTE"
MODE_LTE = "MODE_LTE"
MODES    = (
    MODE_GTE,
    MODE_LTE,
)

################################################################################
### Class
################################################################################

class DichoIter(object):
    ################################################################################
    ### Accessors
    ################################################################################

    @property
    def charset(self):
        if not hasattr(self, "_charset"):
            self._charset = []
        return self._charset

    @charset.setter
    def charset(self, charset):
        self._charset = charset
        if middle(self.charset) == -1:
            return self.abort("Length")
        self.char = self.charset[middle(self.charset)]

    ################################################################################
    ### Methods
    ################################################################################

    def __init__(self, mode, charset = CHARSET, text = ""):
        if mode not in MODES:
            raise Exception("[-] DichoIter: Invalid Mode")
        self.mode         = mode
        self.orig_text    = text
        self.orig_charset = sorted(list(charset))

    def __iter__(self):
        self.stop    = False
        self.text    = self.orig_text
        self.charset = self.orig_charset
        return self

    def next(self):
        if self.stop == True:
            raise StopIteration
        return self.text + self.char

    def eq(self, abort = False):
        self.text   += self.char
        self.charset = self.orig_charset
        if abort == True:
            self.stop = True

    def lt(self, equal = False):
        if self.mode == MODE_LTE and not equal:
            return self.abort("Must Use LTE")
        elif self.mode == MODE_GTE and equal:
            return self.abort("Must Use LT")
        if self.prefix(True, equal):
            self.charset = self.charset[:middle(self.charset) + (1 if equal else 0)]
        self.suffix(True, equal)

    def gt(self, equal = False):
        if self.mode == MODE_GTE and not equal:
            return self.abort("Must Use GTE")
        elif self.mode == MODE_LTE and equal:
            return self.abort("Must Use GT")
        if self.prefix(False, equal):
            self.charset = self.charset[middle(self.charset) + (0 if equal else 1):]
        self.suffix(False, equal)

    def lte(self):
        return self.lt(True)

    def gte(self):
        return self.gt(True)

    def prefix(self, lt, equal):
        # print "%s%s %s" % (("<" if lt else ">"), ("=" if equal else ""), self.char),
        if middle(self.charset) == -1:
            self.abort("%s%s '%s' %s" % (("<" if lt else ">"), ("=" if equal else ""), str(self.char), self.charset))
            return False
        elif len(self.charset) >= 3:
            if not equal:
                if MODE_LTE and not lt:
                    self.charset = self.charset[middle(self.charset):]
                    return False
                elif MODE_GTE and lt:
                    self.charset = self.charset[:middle(self.charset) + 1]
                    return False
        elif len(self.charset) == 2:
            if self.mode == MODE_GTE and lt:
                # print "[*] MODE_GTE: LT: [0]"
                self.char = self.charset[0]
            elif self.mode == MODE_GTE and not lt:
                # print "[!] You Need Me !"
                exit(0)
                # print "[*] MODE_GT: GT: [1]"
                # self.char = self.charset[1]
            elif self.mode == MODE_LTE and lt:
                # print "[!] You Need Me !"
                exit(0)
                # print "[*] MODE_LTE: LT: [1]"
                # self.char = self.charset[1]
            elif self.mode == MODE_LTE and not lt:
                # print "[*] MODE_LTE: GT: [0]"
                self.char = self.charset[0]
            self.eq()
            return False
        return True

    def suffix(self, lt, equal):
        # print self.charset
        if len(self.charset) == 2:
            if self.mode == MODE_GTE:
                # print "[*] MODE_GTE: [1]"
                self.char = self.charset[1]
            if self.mode == MODE_LTE:
                # print "[*] MODE_LTE: [0]"
                self.char = self.charset[0]
        elif len(self.charset) == 1:
            self.eq()

    def abort(self, msg):
        self.stop = True
        print "[!] Error: %s" % msg

################################################################################
### Module
################################################################################

if __name__ == '__main__':
  pass
