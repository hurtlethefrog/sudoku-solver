board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]
#  the solution
# 4 3 5  | 2 6 9  | 7 8 1
# 6 8 2  | 5 7 1  | 4 9 3
# 1 9 7  | 8 3 4  | 5 6 2
# - - - - - - - - - - - - 
# 8 2 6  | 1 9 5  | 3 4 7
# 3 7 4  | 6 8 2  | 9 1 5
# 9 5 1  | 7 4 3  | 6 2 8
# - - - - - - - - - - - - 
# 5 1 9  | 3 2 6  | 8 7 4
# 2 4 8  | 9 5 7  | 1 3 6
# 7 6 3  | 4 1 8  | 2 5 9


def exe(b):
    find = empty(b)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(b, i, (row, col)):
            b[row][col] = i

            if exe(b):
                return True
            
            b[row][col] = 0

    return False


def empty(b):

    for i in range (len(b)):
        for k in range(len(b[0])):
            if b[i][k] == 0:
                #  y coord given first because array of arrays
                return (i, k)

def valid(b, num, pos):

    for i in range(len(b[0])):
        if b[pos[0]][i] == num and pos[1] !=i:
            return False

    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] !=i:
            return False

    coor_x = pos[1] // 3   
    coor_y = pos[0] // 3

    for i in range(coor_y * 3, coor_y * 3 + 3):
        for k in range(coor_x * 3, coor_x * 3 + 3):
            if b[i][k] == num and (i, k) != pos:
                return False
    return True

def visual_board(b):
    # visualize sudoku b when given 9x9 array of arrays
    for i in range(len(b)):
        if i % 3  == 0 and i != 0:
            print('- - - - - - - - - - - - ')

        for k in range(len(b[0])):
            if k % 3 == 0 and k != 0:
                print(' | ', end='')

            if k == 8:
                print(b[i][k])
            else:
                print(str(b[i][k]) + ' ', end='')

visual_board(board)
exe(board)
print('#_-_-_-_-_-_-_-_-_-_-_-_#')
visual_board(board)