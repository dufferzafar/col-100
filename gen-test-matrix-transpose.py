
from random import randint

NUM_CASES = 2

RANGE_OF_SIZES = (5, 999)
RANGE_OF_NUMBERS = (-9000, 9000)

TEST_CASE_FORMAT = """
case = Test %d
grade reduction = 100%%
input = %s
output = %s
"""

for i in range(1, 1+NUM_CASES):

    matrix = []

    # Random size (mxn) of matrix
    m = randint(*RANGE_OF_SIZES)
    n = randint(*RANGE_OF_SIZES)

    # Random matrix
    for _ in range(0, m):
        row = [str(randint(*RANGE_OF_NUMBERS)) for _ in range(0, n)]
        matrix.append(row)

    matrix_str = "\n".join([" ".join(row) for row in matrix])
    inp = "%d %d\n%s" % (m, n, matrix_str)

    transpose = zip(*matrix)
    out = "\n".join([" ".join(row) for row in transpose])

    print(TEST_CASE_FORMAT % (i, inp, out))
