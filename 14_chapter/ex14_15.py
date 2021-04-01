sample = [5, 4, 2, 8, 7, 5, 3, 0, 9, 1]
import itertools
print(list(itertools.accumulate(sample)))
print(list(itertools.accumulate(sample, min)))
print(list(itertools.accumulate(sample, max)))

import operator
print(list(itertools.accumulate(sample, operator.mul)))
print(list(itertools.accumulate(range(1, 11), operator.mul)))