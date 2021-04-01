from array import array
import reprlib
import math
import numbers
import itertools

class Vector:
    typecode = 'd' # for bytearray representation

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components) # print with limited length
        components = components[components.find('['):-1] # print from [ until ]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return math.sqrt(sum(x * x for x in self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, idx):
        cls = type(self)
        if isinstance(idx, slice):
            return cls(self._components[idx])
        elif isinstance(idx, numbers.Integral):
            return self._components[idx]
        else:
            msg = '{cls.__name__} indicies must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))


    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented


    def __radd__(self, other):
        return self + other # must be commutative

v1 = Vector([3, 4, 5])
v2 = Vector([6, 7, 8])
print(v1 + v2)

v1 = Vector([3, 4, 5, 6])
v3 = Vector([1, 2])
print(v1 + v3)

v1 = Vector([3, 4, 5])
print(v1 + (10, 20, 30))
print(v1 + [1, 2, 3, 4, 5, 6, 7, 8, 9])

v1 = Vector([3, 4, 5])
print((10, 20, 30) + v1)

print(v1 + 1)
print(v1 + 'ABC')
