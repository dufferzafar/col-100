from random import randint
from math import sqrt


RAND_RANGE = (-20, 20)

####################################

NUM_CASES = 20

TEST_CASE_FORMAT = """
case = Test %d
input = %s
output = /.*%s.*/
"""

####################################


def q(a, b, c, x):
    return x * x * x + a * x * x + b * x + c


def qq(a, b, c, x):
    return 3 * x * x + 2 * a * x + b


def qqq(a, b, c, x):
    return 6 * x + 2 * a


def qq_root(a, b, c):
    D = b * b - 4 * a * c
    r1 = (-b + sqrt(D)) / 2 * a
    r2 = (-b - sqrt(D)) / 2 * a

    return r1, r2


def func_minima(a, b, c, L, R):

    r1, r2 = qq_root(a, b, c)

    val = []

    if L <= r1 <= R:
        # and qqq(r1) > 0:
        val.append(q(a, b, c, r1))

    if L <= r2 <= R:
        # and qqq(r2) > 0:
        val.append(q(a, b, c, r2))

    val.append(q(a, b, c, L))
    val.append(q(a, b, c, R))

    return min(val)


for i in range(1, 1 + NUM_CASES):

    a = randint(*RAND_RANGE)
    b = randint(*RAND_RANGE)
    c = randint(*RAND_RANGE)

    D = b * b - 4 * a * c

    # No imaginary numbers
    if D < 0:
        continue

    L = randint(*RAND_RANGE)
    R = L + randint(3, 11)

    inp = "\n".join(map(str, [a, b, c, L, R]))
    out = func_minima(a, b, c, L, R)

    print(TEST_CASE_FORMAT % (i, inp, str(out)))


# a = 0
# b = -12
# c = 2
# L = -5
# R = 5

# # print(q(a, b, c, -5))
# # print(func_minima(a, b, c, L, R))
