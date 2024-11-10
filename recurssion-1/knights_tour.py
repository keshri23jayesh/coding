def knights_tour(i, j, board, count):
    if i < 0 or j < 0 or i > len(board) - 1 or j > len(board) - 1:
        return

    if board[i][j] > 0:
        return

    if count == 25:
        board[i][j] = count
        for row in board:
            print(row)
        print("-------")
        board[i][j] = 0
        return

    board[i][j] = count
    knights_tour(i + 1, j + 2, board, count + 1)
    knights_tour(i + 1, j - 2, board, count + 1)
    knights_tour(i - 1, j + 2, board, count + 1)
    knights_tour(i - 1, j - 2, board, count + 1)
    knights_tour(i + 2, j - 1, board, count + 1)
    knights_tour(i + 2, j + 1, board, count + 1)
    knights_tour(i - 2, j - 1, board, count + 1)
    knights_tour(i - 2, j + 1, board, count + 1)
    board[i][j] = 0


board = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

# board = [[0, 0, 0, 0],
#          [0, 0, 0, 0],
#          [0, 0, 0, 0],
#          [0, 0, 0, 0]]

knights_tour(0, 0, board, 1)
