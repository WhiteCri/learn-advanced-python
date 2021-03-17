import array
numbers = array.array('h', [-2, -1, 0, 1, 2]) # 16 bit
octets = bytes(numbers)
print(octets)
