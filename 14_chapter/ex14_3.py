from collections import abc
from abc import abstractmethod
class Iterator(abc.Iterable):

    __slots__ = ()

    @abstractmethod
    def __next(self):
        '''반복자에서 다음 항목을 반환한다. 항목이 소진되면 StopIteration 예외를 발생시킨다.'''
        raise StopIteration

    def __iter__(self):
        return self

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            if (any("__next__") in B.__dict__ for B in C.__mro__) and \
                (any("__iter__") in B.__dict__ for B in C.__mro__):
                return True
            return NotImplemented