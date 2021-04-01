import itertools
print(list(itertools.tee('ABC')))
g1, g2 = itertools.tee('ABC')

print(next(g1))
print(list(g1))

print(next(g2))
print(next(g2))
print(list(g2))

print(list(zip(*itertools.tee('ABC'))))

a = itertools.takewhile(lambda a : a < 10, itertools.count())
print(itertools.takewhile(lambda a : a < 10, itertools.count()))
print(*itertools.takewhile(lambda a : a < 10, itertools.count()))
print(list(itertools.takewhile(lambda a : a < 10, itertools.count())))
print((itertools.takewhile(lambda a : a < 10, itertools.count())))

def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

def chain2(*iterables):
    for it in iterables:
        yield from it

s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))
print(*chain2(s, t))