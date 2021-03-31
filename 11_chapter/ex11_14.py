from random import randrange
from ex11_9 import Tombola

@Tombola.register # abstract subclass of Tombola
class TomboList(list):

    def pick(self):
        if self: # uses __bool__ which is inherited from List
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')
        load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

# Tombola.register(TomboList)

print(issubclass(TomboList, Tombola))
t = TomboList(range(100))
print(isinstance(t, Tombola))
print(TomboList.__mro__)