#!/usr/bin/python2
# coding: utf-8

################################################################################
### Methods
################################################################################

def ceil_modulus(number, modulus = 2):
    """Round number to the next modulus"""
    return number + (modulus - (number % modulus)) % modulus

def floor_modulus(number, modulus = 2):
    """Round number to the prev modulus"""
    return number - number % modulus

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
