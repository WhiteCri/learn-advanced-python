from array import array
import reprlib
import math
import numbers
import functools
import operator

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

    # we want Vector to be immutable, so we won't support writing to instance
    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    ## this one uses super big memory
    # def __eq__(self, other):
    #     return tuple(self) == tuple(other)
    ## version 2
    # def __eq__(self, other):
    #     if len(self) != len(other):
    #         return False
    #     for a, b in zip(self, other): # zip returns generator
    #         if a != b:
    #             return False
    #     return True
    ## version 3, which is shorter version of 2
    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    #
    # def __hash__(self):
    #     hashes = (hash(x) for x in self._components)
    #     return functools.reduce(operator.xor, hashes, 0)
    ## version 2
    def __hash__(self):
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes)