import numpy as np

def check(board, row, col):
    i = 0
    for i in range(row):
        if abs(board[i]-col) == 0 or abs(board[i]-col) == abs(i-row):
            return False
    return True
 
 
def eightqueen(board, row):
    border = len(board)
    if row >= border:
        for i,col in enumerate(board):
            print('□ ' * col + '■ ' + '□ ' * (len(board) - 1 - col))
        print("")
    col = 0
    while col < border:
        for col in range(border):
            if check(board, row, col):
                board[row] = col
                eightqueen(board, row+1)
        col += 1
 
 
 
# board = [0 for i in range(8)]
# print(board)
# eightqueen(board, 0)
a = np.random.randint(1, 9, (3, 3))
print(a)
print(np.flip(a, 2))