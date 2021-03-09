fruits = ['grape', 'raspberry', 'apple', 'banana']

print(sorted(fruits))

print(sorted(fruits, reverse=True))

print(sorted(fruits, key=len))

print(sorted(fruits, key=len, reverse=True))

print(fruits)

fruits.sort()
print(fruits)

import numpy as np
floats = np.loadtxt('floats-10M-lines.txt')
print(floats[-3:])