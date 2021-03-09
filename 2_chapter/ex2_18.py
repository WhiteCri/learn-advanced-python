import bisect
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect_right(breakpoints, score)
    return grades[i]
def grade2(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect_left(breakpoints, score)
    return grades[i]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
print([grade2(score) for score in [33, 99, 77, 70, 89, 90, 100]])