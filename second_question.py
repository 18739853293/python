import struct
q = open('hahaha.txt','rb')
w = q.read(42)
e = struct.unpack('<H10i',w)
print(e)