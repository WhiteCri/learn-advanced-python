s = 'café'
print(len(s))
b = s.encode('utf8') # encode with utf8 bytes code
print(b)
print(len(b))

print(b.decode('utf8'))