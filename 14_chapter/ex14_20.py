import itertools
print(list(itertools.combinations('ABC', 2))) # 3C2
print(list(itertools.combinations_with_replacement('ABC', 2))) #중복조합
print(list(itertools.permutations('ABC', 2)))
print(list(itertools.product('ABC', repeat=2)))
