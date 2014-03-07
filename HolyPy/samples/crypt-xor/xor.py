#!/usr/bin/python2
# coding: utf-8

from passwd             import key
from holypy.core.memory import *
from holypy.crypt.xor   import *
from holypy.core.iter   import *

txt     = "BONJOUR LES AMIS COMMENT ALLER vous. je pense que vous n'etes pas tres tres bien.... peut mieur faire revenez a 10h20. ah oui le fflag est POMPOMPELOPE"
cipher  = xor(txt, key)

breaker = Xor(cipher)
breaker.analyze_length()
breaker.analyze(13)
print
breaker.report()
print
breaker.report_index(0)
print
breaker.report_plain()

# On guess que la clef est de 14
breaker.analyze(14)
print
breaker.report()
print
breaker.report_index(0)
print
breaker.report_plain()
print

# On devine "flag"
breaker.analyze_plain("flag")

# On relance avec les bons chars
breaker.analyze(14, filters = {
    4: {"charset": ["O"]},
    5: {"charset": ["U"]},
    6: {"charset": ["R"]},
    7: {"charset": ["L"]},
})
print
breaker.report()
print
breaker.report_plain()

# Un espace apres "flag"
print
breaker.report_index(8)

# Seul le "E" convient
breaker.analyze(14, filters = {
    4: {"charset": ["O"]},
    5: {"charset": ["U"]},
    6: {"charset": ["R"]},
    7: {"charset": ["L"]},
    8: {"charset": ["E"]},
})
print
breaker.report()
print
breaker.report_plain()

# ...
