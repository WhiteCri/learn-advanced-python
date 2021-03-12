class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key] # call self.__getitem__
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])
#print(d[1])

print(d.get('2'))
print(d.get(4))
print(d.get(1, 'N/A'))

print(2 in d)
print(1 in d)
print(d)

#example of collections.counter

import collections
lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']
print(collections.Counter(lst))
print(collections.Counter({'가': 3, '나': 2, '다': 4}))
c = collections.Counter(a=2, b=3, c=2)
print(collections.Counter(c))
print(sorted(c.elements()))

container = collections.Counter()
container.update('aabcdeffgg')
print(container)

for k, v in container.items():
    print(k, v)