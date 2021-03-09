board = [['_'] * 3 for i in range(3)]
print(board)

board[1][2] = 'X'
print(board)

## actually it's same with..

board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)