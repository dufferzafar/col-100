from random import randint

RAND_RANGE = (10, 50)

####################################

NUM_CASES = 10

TEST_CASE_FORMAT = """
case = Test %d
input = %d
output = /.*%s.*/
"""

####################################

fib_cnt = 0


def fibo(n):
    global fib_cnt
    fib_cnt += 1

    if n <= 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def fibi(n):

    if n <= 2:
        return 1

    a = 1
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c

    return c


for i in range(1, 1 + NUM_CASES):

    inp = randint(*RAND_RANGE)

    # fib_cnt = 0
    val = fibi(inp)

    # out = " ".join([str(val), str(fib_cnt)])
    out = str(val)

    print(TEST_CASE_FORMAT % (i, inp, out))
