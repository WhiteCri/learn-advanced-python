from abc import ABCMeta
class Sized(metaclass=ABCMeta):

    __slots__ = ()
    @abstract_method
    def __len__(self):
        return 0

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Sized:
            if any("__len__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented