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


# def exe():


# def create_board():


def empty():

    for i in range (len(board)):
        for k in range(len(board[0])):
            if board[i][k] == 0:
                return (i, k)

# def valid():


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