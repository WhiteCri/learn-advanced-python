weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = '0'
print(weird_board)

## it's smae with..
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
# see chapter 8...
a = [] * 3
print(a)
#a[0].append(1)
print(a)

b = [1]
a += b # if a implemented __iadd__(), it work with that method,
# if not, then it will be like a = a + b

l = [1, 2, 3]
print(id(l))

l *= 2
print(l)
print(id(l))

t = (1, 2, 3)
print(id(t))

t *= 2
print(id(t)) # different id. new tuple instance made
#but in the case of str, it has memory buffer, so it's ok to do above thing with str()

