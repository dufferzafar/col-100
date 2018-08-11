from random import randint

RAND_RANGE = (0, 100000)

####################################

NUM_CASES = 15

TEST_CASE_FORMAT = """
case = Test %d
input = %d
output = %s
"""

####################################


def fact(n):
    r = 1
    for i in range(1, n + 1):
        r = r * i
    return r


# print(fact(10))

for i in range(1, 1 + NUM_CASES):

    inp = randint(*RAND_RANGE)

    out = 1
    while fact(out) < inp:
        out = out + 1

    print(TEST_CASE_FORMAT % (i, inp, fact(out)))
