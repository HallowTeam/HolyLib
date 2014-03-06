#!/usr/bin/python2
# coding: utf-8

from string             import letters, digits
from holypy.core.iter   import mindex, mitem

################################################################################
### Constants
################################################################################

"""
Note: La dichotomy avec <= c'est moins bien ! (un point c'est tout !)
"""

(RET_EQ, RET_LT, RET_GTE) = xrange(3)

################################################################################
### Class
################################################################################

class Dichotomy(object):

    ############################################################################
    ### Accessors
    ############################################################################

    @property
    def charset(self):
        if not hasattr(self, "_charset"):
            self._charset = []
        return self._charset

    @charset.setter
    def charset(self, charset):
        self._charset = charset
        if mindex(self.charset) == -1:
            raise LookupError("Dichotomy: invalid length")
        self.char = mitem(self.charset)

    ############################################################################
    ### Methods
    ############################################################################

    def __init__(self, fn, charset = letters + digits, text = ""):
        self.fn           = fn
        self.stop         = False
        self.orig_text    = text
        self.text         = self.orig_text
        self.orig_charset = sorted(list(charset))
        self.charset      = self.orig_charset

    def run(self):
        if self.stop == True:
            return True
        try:
            match = ""
            count = [0] * 4
            while not self.stop:
                if count[2] != len(self.text):
                    count[2] = len(self.text)
                    if count[0] == 0 or count[1] == 0:
                        if count[3] == 0:
                            count[3] = 1
                            match = self.text[:-1]
                    else:
                        count[3] = 0
                    count[0] = 0
                    count[1] = 0
                ret = self.fn(self.text + self.char, False)
                if ret not in [RET_LT, RET_GTE]:
                    raise TypeError("Dichotomy: invalid return")
                elif ret == RET_LT:
                    count[0] += 1
                    self.lt()
                elif ret == RET_GTE:
                    count[1] += 1
                    self.gte()
            return True
        except KeyboardInterrupt as e:
            self.text = match
            return True

    def abort(self):
        ret = self.fn(self.text, True)
        if ret == RET_EQ:
            return True
        return False

    def eq(self):
        self.text   += self.char
        self.charset = self.orig_charset
        if self.abort() == True:
            self.stop = True

    def lt(self):
        if len(self.charset) == 2:
            self.char = self.charset[0]
            self.eq()
            return
        self.charset = self.charset[:mindex(self.charset)]
        self.analyze()

    def gte(self):
        if len(self.charset) == 2:
            self.char = self.charset[1]
            self.eq()
            return
        self.charset = self.charset[mindex(self.charset):]
        self.analyze()

    def analyze(self):
        if len(self.charset) == 2:
            self.char = self.charset[1]
        elif len(self.charset) == 1:
            self.eq()

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
