import struct
a = open('pb.txt','rb')
s = a.read(679)
d = struct.unpack('=Hi44s33s43s21s480s52s',s)
print(d[0],d[1])
print(d[2].decode('utf-8'))
print(d[3].decode('utf-8'))
print(d[4].decode('utf-8'))
print(d[5].decode('utf-8',errors='ignore'))
print(d[6].decode('utf-8',errors='ignore'))
print(d[7].decode('utf-8',errors='ignore'))