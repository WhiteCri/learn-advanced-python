l = ['span', 'span', 'eggs', 'span']
print(set(l)) # the element in set have to be hashable
print(list(set(l)))


haystack = set() # some big set
needles = set() # some small set

found = len(needles & haystack) #this is same with below code
found = 0
for n in needles:
    if n in haystack:
        found += 1
#or this code...
found = len(set(needles) & set(haystack))
# or
found = len(set(needles).intersection(haystack))

s = {1}
print(type(s))
print(s)
s.pop()
print(type(s))

from dis import dis
dis('{1}')
dis('set([1])')
dis('set(1)')

print(frozenset(range(10)))