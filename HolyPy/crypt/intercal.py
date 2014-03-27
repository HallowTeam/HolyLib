#!/usr/bin/python2
# coding: utf-8
# source: https://ideone.com/
# source: http://progopedia.com/language/intercal/
# source: http://divingintointercal.blogspot.fr/2007/03/part-dalawa-still-trying-to-write-hello.html

################################################################################
### Functions
################################################################################

def binarize(value):
    return bin(value & 0b11111111)[2:].rjust(8, "0")

def convert_to_output(array):
    prev   = chr(0)
    string = ""
    for i, index in enumerate(array):
        char    = int(binarize(ord(prev))[::-1], 2)
        char    = int(binarize(char - index)[::-1], 2)
        char    = chr(char % 256)
        prev    = char
        string += char
    return string

def convert_to_input(string):
    array = []
    for i, c in enumerate(string):
        char      = int(binarize(ord(c))[::-1], 2)
        prev_char = int(binarize(ord(string[i - 1] if i != 0 else chr(0)))[::-1], 2)
        array.append((prev_char - char) % 256)
    return array

################################################################################
### History
################################################################################

# def indexOfChar(char, prev_char):
#     char      = int(binarize(ord(char     ))[::-1], 2)
#     prev_char = int(binarize(ord(prev_char))[::-1], 2)
#     index     = prev_char - char
#     return index % 256

# def indexToChar(index, prev_char):
#     prev_char = int(binarize(ord(prev_char))[::-1], 2)
#     char      = int(binarize(prev_char - index)[::-1], 2)
#     return chr(char % 256)

# text   = "Hello, World!"
# prev  = 0
# cipher = []
# for i, c in enumerate(text):
#     index = indexOfChar(c, text[i - 1] if i != 0 else chr(0))
#     cipher.append(index)
# print cipher

# text = ""
# prev = chr(0)
# for i, index in enumerate(cipher):
#     text += indexToChar(index, prev)
#     prev  = text[-1]
# print text

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
