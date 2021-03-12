from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d) # shallow copy
print(d_proxy)

print(d_proxy[1])

#d_proxy[2] = 'b'

d[2] = 'B'
print(d_proxy)
print(d_proxy[2])

