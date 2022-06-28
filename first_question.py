import struct
from ctypes import *


class demo1(Structure):
    _fields_ = [("byProtocol", c_ubyte),
                ("nRetCode", c_int),
                ("szAccount", c_char * 80),
                ("szRandomKey", c_char * 50)]


f = open('hahaha2.txt', 'rb')
b = f.read(135)
byProtocol,nRetCode,szAccount,szRandomKey = struct.unpack('=Bi80s50s',b)
print(byProtocol)
print(nRetCode)
print(szAccount.decode('utf-8'))
print(szRandomKey.decode('utf-8'))


