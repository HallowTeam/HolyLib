#!/usr/bin/python2
# coding: utf-8

import re
import binascii

################################################################################
### Class
################################################################################

class Parser():
  def __init__(self, dataRaw, dataSize = 2, nameSize = 12):
    self.data        = {}
    self.names       = []
    self.dataLen     = 0
    self.dataRaw     = dataRaw
    self.nameSize    = nameSize
    self.dataSize    = dataSize
    self.dataOrig    = dataRaw
    self.dataOrigLen = len(dataRaw)

  def extract(self, chunks):
    for chunk in chunks:
      self.extractData(*chunk)

  def extractData(self, name, size, callbacks = [], end = False):
    if name in self.data.keys():
      name = name + "_" + "1"
      while name in self.data.keys():
        name, suffix = name.rsplit('_', 1)
        name = name + "_" + str(int(suffix) + 1)
    if not isinstance(size, int):
      if not isinstance(size, list):
        size = [size]
      temp = size
      for func in size:
        temp = func(self, temp, self.dataSize)
      size = temp
    if size == 0:
      data = self.dataRaw
    else:
      if not end:
        self.data[name] = self.dataRaw[:size * self.dataSize]
        self.dataRaw    = self.dataRaw[size * self.dataSize:]
      else:
        self.data[name] = self.dataRaw[-size * self.dataSize:]
        self.dataRaw    = self.dataRaw[:-size * self.dataSize]
      self.dataLen += len(self.data[name]) / self.dataSize
      self.names.append(name)
      data = self.data[name]
    if callbacks != None:
      if not isinstance(callbacks, list):
        callbacks = [callbacks]
      for callback in callbacks:
        data = callback(self, data, self.dataSize)
      print "{:<2d} - {:{:d}s}: {:s}".format(size, name, self.nameSize, data)

  def toggleEndian(self, data):
    return "".join(self.extractBytes(data)[::-1])

  def extractBytes(self, data):
    if len(data) % self.dataSize != 0:
      print "Warning: odd number of chars"
    return re.findall('.' * self.dataSize, data)

  def sizeByKey(self, key, base = 16, endian = True):
    def _sizeByKey(self, data, size):
      size = self.data[key]
      if endian == True:
        size = self.toggleEndian(size)
      return int(size, base)
    return _sizeByKey

  def sizeByIndex(self, index, base = 16, endian = True):
    def _sizeByIndex(self, data, size):
      size = self.data[self.names[index]]
      if endian == True:
        size = self.toggleEndian(size)
      return int(size, base)
    return _sizeByIndex

  def sizeByPadding(self, padding):
    def _sizeByPadding(self, data, size):
      return padding - self.dataLen % padding
    return _sizeByPadding

  def formatHex(self, endian = True):
    def _formatHex(self, data, size):
      if endian == True:
        data = self.toggleEndian(data)
      return "%s (%d)" % (data, int(data, 16))
    return _formatHex

  def formatAscii(self, endian = False):
    def _formatAscii(self, data, size):
      if endian == True:
        data = self.toggleEndian(data)
      return binascii.unhexlify(data)
    return _formatAscii

################################################################################
### Module
################################################################################

if __name__ == '__main__':
    pass
