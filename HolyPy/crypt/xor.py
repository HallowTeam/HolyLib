#!/usr/bin/python2
# coding: utf-8

import string

from holypy.core.iter   import split
from holypy.core.memory import xor
from holypy.core.output import *

################################################################################
### Constantes
################################################################################

KEYSET = set(string.letters + string.digits + "_")
TXTSET = set(string.letters + string.digits + "_ ',.!")

################################################################################
### Methodes
################################################################################

# def analyze(cipher, keylen, keyset = KEYSET, txtset = TXTSET, idxban = None, idxset = None):
#     """Recherche une clef probable"""
#     missing = -1
#     chunks  = split(cipher, keylen)
#     charset = set()
#     ignored = set()
#     matches = [[] for i in xrange(keylen)]
#     for i in xrange(keylen):
#         for k in keyset:
#             if not (idxset and i in idxset.keys()) or k in idxset[i]:
#                 if not (idxban and i in idxban.keys() and k in idxban[i]):
#                     success  = False
#                     ichars   = []
#                     icharset = set()
#                     for chunk in chunks:
#                         if i >= len(chunk):
#                             break
#                         success = True
#                         c = xor(chunk[i], k)
#                         if not c in txtset:
#                             ignored |= set(c)
#                             success  = False
#                             break
#                         icharset |= set(c)
#                         ichars.append(c)
#                     if success:
#                         charset |= icharset
#                         matches[i].append({
#                             "key"    : k,
#                             "chars"  : ichars,
#                             "charset": icharset,
#                         })
#         if len(matches[i]) == 0:
#             missing = i
#             break
#     return (matches, charset, ignored, missing)

# def report(matches, charset, ignored, missing, idx = None):
#     """Affiche le bilan de l'analyze"""
#     if missing != -1:
#         print fmt("[-] Xor: failure at index %d" % missing, RED)
#     else:
#         print fmt("[+] Xor: success", GREEN)
#     _report_guess(matches)
#     _report_infos(charset, ignored)
#     if idx != None:
#         _report_index(matches, idx)

# def guess(matches, charset, ignored, missing, hint = None):
#     if hint != None:
#         matches = _guess_with_hint(matches, hint)
#     plain   = ""
#     guesses = []
#     for matchset in matches:
#         if len(matchset) != 0:
#             guess = [[-1, False] for i in xrange(len(matches[0][0]["chars"]))]
#             for match in matchset:
#                 for i, c in enumerate(match["chars"]):
#                     if guess[i][0] == None:
#                         break
#                     elif guess[i][0] == -1:
#                         guess[i][0] = c
#                     elif guess[i][0] != c:
#                         if guess[i][0].lower() == c.lower():
#                             guess[i][1] = True
#                         else:
#                             guess[i][0] = None
#             guesses.append(guess)
#     for i in xrange(len(guesses)):
#         for charset in guesses:
#             if i < len(charset):
#                 c    = charset[i][0]
#                 case = charset[i][1]
#                 if c == -1:
#                     pass
#                 elif c == None:
#                     plain += fmt("?", WHITE)
#                 else:
#                     if case == False:
#                         plain += fmt(c, BLUE)
#                     else:
#                         plain += fmt(c, YELLOW)
#     print "[+] " + plain

# def _guess_with_hint(cipher, matches, hint = ""):
#     key   = []
#     index = -1
#     for i in xrange(len(cipher)):
#         success  = False
#         matchset = getitem(matches, i)
#         for k in sorted([x["key"] for x in matchset]):
#             char = xor(cipher[i], k)
#             if index == -1 and char in pattern:
#                 success = True
#                 index   = pattern.index(char)
#                 key.append(k)
#                 break
#             elif index != -1 and char == getitem(pattern, index + 1):
#                 success = True
#                 index  += 1
#                 key.append(k)
#                 break
#         if success == False:
#             index = -1
#             key   = []
#         elif len(key) == len(pattern):
#             offset = ((i + 1) - len(pattern)) % len(matches)
#             for i, matchset in enumerate(matches):
#                 if i in xrange(offset, offset + len(pattern)):
#                     matchset = [key[i - offset]]
#             break
#     return matches

# def _report_guess(matches):
#     guess = ""
#     for matchset in matches:
#         if len(matchset) == 1:
#             guess += fmt(matchset[0]["key"], BLUE)
#         else:
#             guess += fmt("?", WHITE)
#     print "[*] " + guess
#     print
#     for i, matchset in enumerate(matches):
#         if len(matchset) == 1:
#             print "[%d]" % i, fmt(sorted([x["key"] for x in matchset]), BLUE)
#         else:
#             print "[%d]" % i, fmt(sorted([x["key"] for x in matchset]), WHITE)

# def _report_index(matches, index):
#     for infos in matches[index]:
#         print
#         print fmt("[%c]" % infos["key"], MAGENTA)
#         print fmt(sorted([x for x in infos["charset"]]), WHITE)

# def _report_infos(charset, ignored):
#     print
#     print fmt("[charset]", MAGENTA)
#     print fmt(sorted([x for x in charset]), WHITE)
#     print
#     print fmt("[ignored]", MAGENTA)
#     print fmt(sorted([x for x in ignored]), WHITE)

# ################################################################################
# ### Module
# ################################################################################

# if __name__ == '__main__':
#     pass
