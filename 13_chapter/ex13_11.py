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

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

    def __matmul__(self, other):
        try:
            return sum(a * b for a, b in zip(self, other))
        except TypeError:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other

    def __eq__(self, other):
        if isinstance(other, Vector):
            return (len(self) == len(other)) and all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented


v1 = Vector([1, 2, 3])
print(v1 * 10)
print(11 * v1)

v1 = Vector([1., 2., 3.])
print(14 * v1)
print(v1 * True)
from fractions import Fraction
print(v1 * Fraction(1, 3))

va = Vector([1, 2, 3])
vz = Vector([5, 6, 7])
print(va @ vz == 38.0)
print([10, 20, 30] @ vz)

va = Vector([1., 2. , 3.])
vb = Vector(range(1, 4))
print(va == vb)
vc = Vector([1, 2])
print(vc == [1, 2])

print('----- *= test -----')

v1 = Vector([1, 2, 3])
v1_alias = v1
print(id(v1), id(v1_alias))
v1 += Vector([4, 5, 6])
print(v1)
print(id(v1))

print(v1_alias)
v1 *= 11 # if we didn't define __iaddr__(), a += b is equal to a = a + b
print(v1)
print(id(v1))