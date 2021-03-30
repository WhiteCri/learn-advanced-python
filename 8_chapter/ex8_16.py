# del() removes the reference,
# and when reference equals 0, then __del__() is called

import weakref
s1 = {1, 2, 3}
s2 = s1
def bye():
    print('Gone with the wind...')

ender = weakref.finalize(s1, bye)
print(ender.alive)

del s1
print(ender.alive)

s2 = ' spam'
print(ender.alive)

# weak ref maintains the reference to instance, without increasing the reference count
