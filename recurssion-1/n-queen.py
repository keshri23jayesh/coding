def is_safe_place(board, row, col):
    # check col
    for i in range(0, len(board)):
        if board[i][col] == 1:
            return False

    # Check left upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right upper diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True


def place_queens(row, board, qsf):

    if row == len(board):
        for row in board:
            print(row)
        print("---")
        return

    for col in range(0, len(board)):
        if is_safe_place(board, row, col):
            board[row][col] = 1
            place_queens(row + 1, board, qsf + str(row) + '-' + str(col) + '*')
            board[row][col] = 0


board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

place_queens(0, board, '')
