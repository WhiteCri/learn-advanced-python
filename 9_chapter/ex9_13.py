from array import array
import math

## when using __slots__...
# __slots__ are not inherited
# unless we define __dict__ in slots, we can use only what is in the slots
# unless we define __weakref__ in slots, a class can not be pointed with weakref
class Vector2d:
    #__slots__ = ('__x', '__y') # it must be used only with immutable instance
    # and also we need to define __weakref__ in __slots__ when we want to use
    typecode = 'd'# this is class variable

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

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

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
print(dumpd)
len(dumpd)
v1.typecode = 'f' #this is instance variable. can not be used with __slots__
dumpf = bytes(v1)
print(dumpf)
print(len(dumpf))
print(Vector2d.typecode)

class ShortVector2d(Vector2d):
    typecode = 'f'

print('---ShortVector2d---')
sv = ShortVector2d(1/11, 1/27)
print(sv)
print(len(bytes(sv)))