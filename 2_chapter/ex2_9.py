from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
#namedtuple('City', ['name','country','population','coordinates']) is also ok
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
