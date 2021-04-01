print(all([1, 2, 3]))
print(all([1, 0, 3]))

def hmm():
    for i in range(5):
        yield True
    print('hmmmmm')
    yield False

print(all(hmm()))

print(all([]))
print(any([1, 2, 3]))
print(any([1, 0, 3]))
print(any([0, 0.0]))
print(any([]))
g = (n for n in [0, 0.0, 7, 8])
print(any(g))
print(next(g))
#print(next(g))


from random import randint
def d6():
    return randint(1, 6)

d6_iter = iter(d6, 1)
print('----d6---')
print(d6_iter)
for roll in d6_iter:
    print(roll)