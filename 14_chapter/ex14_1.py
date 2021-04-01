import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

s = Sentence('"The time has come, " the Walrus said,')
print(s)

for word in s:
    print(word)
print(list(s))
print(s[0], s[1], s[-1])

# when python interpreter want to iterate, it calls iter(x)
# iter(x) is processed with...
# 1. check __iter__()
# 2. check __getitem()
# 3. TypeError. C object is not iterable

class Foo:
    def __iter__(self):
        pass

from collections import abc
print(issubclass(Foo, abc.Iterable))
f = Foo()
print(isinstance(f, abc.Iterable))

s = 'abc'
for ch in s:
    print(ch)

s = 'ABC'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break

s3 = Sentence('Pig and Pepper')
it = iter(s3)
print(it)
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration:
    pass
print(list(it))
print(list(iter(s3)))