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


# The given polynomial
def q(a, b, c, x):
    return x * x * x + a * x * x + b * x + c


# 1st Derivative of the polynomial
def qq(a, b, c, x):
    return 3 * x * x + 2 * a * x + b


# 2nd Derivative of the polynomial
def qqq(a, b, c, x):
    return 6 * x + 2 * a


# Find root of the 1st Derivative
def qq_root(a, b, c):
    D = 4 * a * a - 12 * b
    r1 = (-2 * a + sqrt(D)) / 6
    r2 = (-2 * a - sqrt(D)) / 6

    return r1, r2


# Find minimum value of function
def func_minima(a, b, c, L, R):
    val = []

    # Roots
    r1, r2 = qq_root(a, b, c)

    if L <= r1 <= R:
        val.append(q(a, b, c, r1))

    if L <= r2 <= R:
        val.append(q(a, b, c, r2))

    val.append(q(a, b, c, L))
    val.append(q(a, b, c, R))

    return min(val)


case = 1
for i in range(1, 1 + NUM_CASES):

    # Generate 3 random numbers
    a = randint(*RAND_RANGE)
    b = randint(*RAND_RANGE)
    c = randint(*RAND_RANGE)

    D = 4 * a * a - 12 * b

    # No imaginary numbers
    if D < 0:
        continue

    # Generate a random range
    L = randint(*RAND_RANGE)
    R = L + randint(3, 11)

    inp = "\n".join(map(str, [a, b, c, L, R]))
    out = func_minima(a, b, c, L, R)

    if isinstance(out, int):
        out = "%d" % out
    elif isinstance(out, float):
        out = "%.2f" % out

    print(TEST_CASE_FORMAT % (case, inp, out))

    case += 1


# Used while debugging:

# a = 0
# b = -12
# c = 2
# L = -5
# R = 5

# a = 16
# b = 4
# c = -16
# L = 13
# R = 19

# print(qq_root(a, b, c))
# print(q(a, b, c, 13))
# print(func_minima(a, b, c, L, R))
