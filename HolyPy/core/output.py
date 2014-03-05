#!/usr/bin/python2
# coding: utf-8
# source: https://gist.github.com/christian-oudard/220521

from holypy.core.iter import iterize

################################################################################
### Constants
################################################################################

(BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, LIGHT_GRAY, DARK_GRAY, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, WHITE) = range(16)
(NONE, BOLD, DARK, UNDEF, UNDERLINE, UNDEF, BLINK, REVERSE, CONCEALED)                                                                                            = xrange(9)

################################################################################
### Methodes
################################################################################

def gray(value):
    """
    Retourne la couleur grise correspondante
    0 <= value <= 23
    """
    return 232 + value

def xrgb(red, green, blue):
    """
    Retourne la couleur RGB correspondante
    0 <= R <= 255
    0 <= G <= 255
    0 <= B <= 255
    """
    return rgb(int(red / 255.0 * 5.0), int(green / 255.0 * 5.0), int(blue / 255.0 * 5.0))

def rgb(red, green, blue):
    """
    Retourne la couleur RGB correspondante
    0 <= R <= 5
    0 <= G <= 5
    0 <= B <= 5
    """
    return 16 + (red * 36) + (green * 6) + blue

def fmt(text, foreground = None, background = None, attributes = (BOLD)):
    """Formate le texte avec les options renseignees"""
    output = ""
    if foreground:
        output += "\x1B[38;5;%dm" % (foreground)
    if background:
        output += "\x1B[48;5;%dm" % (background)
    for attribute in iterize(attributes):
        output += "\x1B[%dm" % (attribute)
    output += str(text)
    output += "\x1B[0m"
    return output

################################################################################
### Helpers
################################################################################

def pprint(text, foreground = None, background = None, attributes = (BOLD)):
    """Affiche un message formate"""
    print fmt(text, foreground, background, attributes)

def pperr(text):
    """Affiche un message d'erreur"""
    pprint(text, RED)

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
