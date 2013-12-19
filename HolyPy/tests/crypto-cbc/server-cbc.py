#!/usr/bin/python2
# coding: utf-8
#source: http://esec-lab.sogeti.com/post/2010/12/03/Padding-Oracle-attack-and-its-applications-on-ASP.NET

import sys
from   Crypto.Cipher     import DES3

################################################################################
################################################################################
################################################################################

class MyPaddingOracleServer:
  key = 'iloveyouihateyou'
  iv = '1712180527255516'.decode('hex')

  def pkcs7(self,text,length):
    if ( (len(text) % 8) == 0 ):
      amount = 8
    else:
      amount = length - len(text)%length
    pattern = chr(amount)
    pad = pattern*amount
    return text + pad

  def encrypt(self,plain):
    cipher = DES3.new(self.key,DES3.MODE_CBC,self.iv)
    paddedPlainText = self.pkcs7(plain,DES3.block_size)
    cipheredText = cipher.encrypt(paddedPlainText)
    return self.iv.encode('hex') + cipheredText.encode('hex')

  def is_pkcs7_padding_valid(self,block):
    c = block[-1]
    return block[-ord(c):] == ord(c) * c

  def decrypt(self,ciphered):
    ciphered = ciphered.decode('hex')
    self.iv = ciphered[0:DES3.block_size]
    cipher = DES3.new(self.key,DES3.MODE_CBC,self.iv)
    uncipher = cipher.decrypt(ciphered[DES3.block_size:])
    if not self.is_pkcs7_padding_valid(uncipher):
      raise Exception("Padding Error")
    else:
      return uncipher.encode('hex')

################################################################################
################################################################################
################################################################################

if len(sys.argv) != 3:
    print "%s: -<c|d> [<cipher>]"
    exit(0)

if sys.argv[1] == "-c":
    oracle = MyPaddingOracleServer()
    print oracle.encrypt(sys.argv[2])

if sys.argv[1] == "-d":
    oracle = MyPaddingOracleServer()
    print oracle.decrypt(sys.argv[2])
