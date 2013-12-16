#!/usr/bin/python2
# coding: utf-8

################################################################################
### Methods
################################################################################

def ceil_modulus(number, modulus = 2):
    """
    Arrondi @number au multiple immediatement superieur de @modulus
    """
    return number + (modulus - (number % modulus)) % modulus

def floor_modulus(number, modulus = 2):
    """
    Arrondi @number au multiple immediatement inferieur de @modulus
    """
    return number - number % modulus

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
