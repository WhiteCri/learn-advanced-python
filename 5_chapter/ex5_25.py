from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))

hiphenate = methodcaller('replace', ' ', '-')
print(print(hiphenate(s)))