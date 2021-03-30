def f(a, b):
    a += b
    return a

x = 1
y = 2
print(f(x, y))
print(x, y) #x, y are not changed

a = [1, 2]
b = [3, 4]
print(f(a, b))
print(a, b) # list a was changed

t = (10, 20)
u = 30, 40
print(f(t, u))
print(t, u) # tuples are not changed