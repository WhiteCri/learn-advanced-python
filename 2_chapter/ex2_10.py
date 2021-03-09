from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
#namedtuple('City', ['name','country','population','coordinates']) is also ok

print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data) # City(*delhi_data)
print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ':', value)

l = [10, 20, 30, 40, 50, 60]
print(l[:2])
print(l[2:])
print(l[:3])
print(l[3:])

s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

