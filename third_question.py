import struct
f = open('g2cSendServerListRespond.txt', 'rb')
s = f.read(132)
a= struct.unpack('=HBhi0BIIB32sIIB32sIIB32s',s)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4],a[5],a[6],a[7].decode('utf-8',errors='ignore'))
print(a[8],a[9],a[10],a[11].decode('utf-8',errors='ignore'))
print(a[12],a[13],a[14],a[15].decode('utf-8',errors='ignore'))
