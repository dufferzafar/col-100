from random import randrange

RAND_RANGE = (3, 100, 2)

####################################

NUM_CASES = 20

TEST_CASE_FORMAT = """
case = Test %d
input = %d
output = /.*%s.*/
"""

####################################


def spiral_dia_sum(n):

    if n % 2 == 0:
        return -1
    elif n == 1:
        return 1
    else:
        # as order should be only odd
        # we should pass only odd-integers
        return 4 * n * n - 6 * n + 6 + spiral_dia_sum(n - 2)


for i in range(1, 1 + NUM_CASES):

    inp = randrange(*RAND_RANGE)

    val = spiral_dia_sum(inp)
    out = str(val)

    print(TEST_CASE_FORMAT % (i, inp, out))
