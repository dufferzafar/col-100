from itertools import product
import random

NUM_CASES = 20

TEST_CASE_FORMAT = """
case = Test %d
input = %s
output = "%s"
"""


def check_board(grid):
    """
    Validate a sudoku solution.

    Given a grid as a list of lists, return None if it is ill-formed,
    False if it is invalid, or True if it is a valid solution.
    """
    assert isinstance(grid, list)

    # Check that the grid is 9x9.
    if len(grid) != 9 or not all(len(row) == 9 for row in grid):
        return None

    DIGITS = set(range(1, 10))

    # Check that each number appears exactly once per row
    if not all(set(row) == DIGITS for row in grid):
        return False

    # Check that each number appears exactly once per column
    columns = [[row[c] for row in grid] for c in range(9)]
    if not all(set(col) == DIGITS for col in columns):
        return False

    # Check that each number appears exactly once per 3x3 grid
    THREES = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    for row_block, col_block in product(THREES, THREES):
        block = [grid[r][c] for r, c in product(row_block, col_block)]
        if set(block) != DIGITS:
            return False

    return True


def good_board(m=3):
    """Return a random correctly filled m**2 x m**2 Sudoku board."""
    n = m**2
    board = [[None for _ in range(n)] for _ in range(n)]

    def search(c=0):
        """Recursively search for a solution starting at position c."""
        i, j = divmod(c, n)
        i0, j0 = i - i % m, j - j % m  # Origin of mxm block

        numbers = list(range(1, n + 1))
        random.shuffle(numbers)

        for x in numbers:
            if (x not in board[i] and                  # row
                all(row[j] != x for row in board) and  # column
                all(x not in row[j0:j0 + m]            # block
                    for row in board[i0:i])):
                board[i][j] = x
                if c + 1 >= n**2 or search(c + 1):
                    return board
        else:
            # No number is valid in this cell: backtrack and try again.
            board[i][j] = None
            return None

    return search()


def bad_board(m=3):
    """Generate a random m**2 x m**2 Sudoku board."""

    n = m**2
    board = []

    numbers = list(range(1, n + 1))

    for _ in numbers:
        random.shuffle(numbers)
        board.append(list(numbers))

    return board


def str_board(brd):
    rv = []
    for row in brd:
        rv.append(" ".join(map(str, row)))

    return "\n".join(rv)


if __name__ == '__main__':
    for i in range(1, 1 + NUM_CASES):

        if bool(random.getrandbits(1)):
            brd = good_board()
        else:
            brd = bad_board()

        inp = str_board(brd)
        out = "Yes" if check_board(brd) else "No"

        print(TEST_CASE_FORMAT % (i, inp, out))
