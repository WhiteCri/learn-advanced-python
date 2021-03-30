class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

import weakref
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
           Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog:
    stock[cheese.kind] = cheese # cheese become the global variable

print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
del cheese
print(sorted(stock.keys()))


## 기본적으로 list나 dict는 약한 참조의 대상이 될 수 없다.
class MyList(list):
    '''약한 참조의 대상이 될 수 있는 list 서브클래스'''

a_list = MyList(range(10))
wref_to_a_list = weakref.ref(a_list)

## set can be a target of weakref
a = [1, 2, 3]
b = a[::-1]
c = 1, 2
print(id(a), id(b), id(a[:]), id(c[:]), id(c))