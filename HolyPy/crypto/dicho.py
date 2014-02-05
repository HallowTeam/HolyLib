#!/usr/bin/python2
# coding: utf-8

import string

################################################################################
### Constants
################################################################################

CHARSET = list(string.letters + string.digits)

################################################################################
### Class
################################################################################

class DichoIter():
    """
    Because of how is computed the middle item we can only use < and >=
    """
    def __init__(self, charset = CHARSET, text = ""):
        self.orig_text    = text
        self.orig_charset = list(charset)
        self.orig_charset.sort()
        self.text         = self.orig_text
        self.charset      = self.orig_charset

    def middle(self):
        return (len(self.charset) - 1) / 2

    def __iter__(self):
        self.text = self.orig_text
        self.reset()
        return self

    def reset(self):
        self.count   = 0
        self.charset = self.orig_charset

    def next(self):
        return self.text + self.char()

    def char(self, offset = True):
        return self.charset[self.middle() + (self.count if offset else 0)]

    def eq(self, offset = True):
        """
        Do not use parameter when using in code
        """
        self.text += self.char(offset)
        self.reset()

    def lt(self):
        if self.count == 1:
            self.charset = self.charset[0]
        else:
            self.charset = self.charset[:self.middle()]
        if len(self.charset) == 2:
            self.count += 1
        elif len(self.charset) == 1:
            self.eq(False)

    def gte(self):
        if self.count == 1:
            self.charset = self.charset[1]
        else:
            self.charset = self.charset[self.middle():]
        if len(self.charset) == 2:
            self.count += 1
        elif len(self.charset) == 1:
            self.eq(False)

    # def lt(self, equal = False):
    #     if self.count == 1:
    #         self.charset = self.charset[0]
    #     else:
    #         self.charset = self.charset[:self.middle() + (1 if equal else 0)]
    #     if len(self.charset) == 2:
    #         self.count += 1
    #     elif len(self.charset) == 1:
    #         self.eq(False)

    # def gt(self, equal = False):
    #     if self.count == 1:
    #         self.charset = self.charset[1]
    #     else:
    #         self.charset = self.charset[self.middle() + (0 if equal else 1):]
    #     if len(self.charset) == 2:
    #         self.count += 1
    #     elif len(self.charset) == 1:
    #         self.eq(False)

################################################################################
### Module
################################################################################

if __name__ == '__main__':
  pass
