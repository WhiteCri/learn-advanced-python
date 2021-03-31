from array import array
import reprlib
import math

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
        return self._components[idx]

v1 = Vector([3, 4, 5])
print(len(v1))
print(v1[0], v1[-1])

v7 = Vector(range(7))
print(v7[1:4]) # result of slicing is not Vector