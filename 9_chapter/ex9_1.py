from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x) # good for detect invalid data type
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self) #!r uses repr()
        # *self can be processed thanks to __iter__()

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, format_spec=''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)


v1 = Vector2d(3, 4)
print(v1.x, v1.y)

x, y = v1
print(x, y)
print(v1)

v1_clone = eval(repr(v1))
print(repr(v1))
print(v1 == v1_clone)
print(v1)

octets = bytes(v1)
print(octets)

print(abs(v1))
print(bool(v1), bool(Vector2d(0, 0)))

print(format(v1, '.3f'))

v1 = Vector2d(3, 4)
print(format(v1))
print(format(v1, '.2f'))
print(format(v1, '.3e'))

print(format(Vector2d(1, 1), 'p'))
print(format(Vector2d(1, 1), '.3ep'))
print(format(Vector2d(1, 1), '0.5fp'))

v1 = Vector2d(3, 4)
#print(hash(v1))
set([v1])