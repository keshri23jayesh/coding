
def is_valid_option(si, sj, s0, sudoko):
    # row check
    for col in range(0, len(sudoko[0])):
        if sudoko[si][col] == s0:
            return False

    # column check
    for row in range(0, len(sudoko)):
        if sudoko[row][sj] == s0:
            return False

    # small matrix check - Trick to remember
    si_start = 3 * (si//3)
    sj_start = 3 * (sj//3)
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoko[si_start+i][sj_start+j] == s0:
                return False

    return True


def solve_sudoko(i, j, sudoko):
    if i == len(sudoko):
        print(sudoko)
        return

    if j == len(sudoko[0]) - 1:
        si = i + 1
        sj = 0
    else:
        si = i
        sj = j + 1

    if sudoko[i][j] != 0:
        solve_sudoko(si, sj, sudoko)
    else:
        # filling logic
        for s0 in range(0, 10):
            if is_valid_option(i, j, s0, sudoko):
                sudoko[i][j] = s0
                solve_sudoko(si, sj, sudoko)
                sudoko[i][j] = 0


board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

solve_sudoko(0, 0, board)
