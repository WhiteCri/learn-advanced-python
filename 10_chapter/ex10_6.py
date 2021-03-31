from array import array
import reprlib
import math
import numbers

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


v7 = Vector(range(7))
print(v7[-1].__repr__())
print(v7[1:4].__repr__())
print(v7[-1:].__repr__())
#print(v7[1, 2].__repr__())

v = Vector(range(5))
print(v)
print(v.x)
v.x = 10 # now v.x is binded to 10
print(v)