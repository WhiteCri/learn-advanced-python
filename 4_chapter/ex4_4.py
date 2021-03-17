import struct
fmt = '<3s3sHH' # < represents little endian, 3s means 3bytes sequence, HH means 16bit integer
with open('filter.fig', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10] # no memory copy occurs
print(bytes(header)) # need to transform to bytes to print. 10 byte copying occurs

print(struct.unpack(fmt, header)) #종류 , 버전, 너비, 높이
del header # remove the reference
del img