from random import randint
import math

RAND_RANGE = (1, 50)

####################################

NUM_CASES = 20

TEST_CASE_FORMAT = """
case = Test %d
input = %d
output = /.*%s.*/
"""

####################################


def is_perf_square(n):
    s = math.floor(math.sqrt(n))
    return s * s == n


def is_fib(n):
    return is_perf_square(5 * n * n + 4) or is_perf_square(5 * n * n - 4)


for i in range(1, 1 + NUM_CASES):

    inp = randint(*RAND_RANGE)
    out = "Yes" if is_fib(inp) else "No"

    print(TEST_CASE_FORMAT % (i, inp, out))
