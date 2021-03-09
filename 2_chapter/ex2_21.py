import array
numbers = array.array('h', [-2, -1, 0, 1, 2]) # short int
#short int : 16 bit
# 1 : 0000 0000 0000 0001
# -1: 1111 1111 1111 1111
# -2: 1111 1111 1111 1110
#      255       254
#      254       255
# -2: 1111 1110 1111 1111 #little endian

# 2 : 0x0  0x0  0x0  0010
#                    0000

memv = memoryview(numbers)
print(len(memv))

print(memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)