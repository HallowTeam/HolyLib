#!/usr/bin/python2
# coding: utf-8

from passwd             import key
from holypy.core.memory import *
from holypy.crypt.xor   import *
from holypy.core.iter   import *

txt = "BONJOUR LES AMIS COMMENT ALLER vous. je pense que vous n'etes pas tres tres bien.... peut mieur faire revenez a 10h20."
cip = xor(txt, key)

data = analyze(cip, len(key), txtset = TXTSET - set("KXZQ"),  idxban = {
    # 0: ["E"],
}, idxset = {
    9: ["S"],
    # 12: ["I"],
})

report(*data, idx = 9)
print
guess(*data, hint = "vous", cipher = cip)




# for i, matchset in enumerate(matches):
#     if len(matchset) == 1:
#         print "[%d]" % i, fmt(sorted([x["key"] for x in matchset]), BLUE)
#     else:
#         print "[%d]" % i, fmt(sorted([x["key"] for x in matchset]), WHITE)
