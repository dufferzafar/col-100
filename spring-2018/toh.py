from random import randint

RAND_RANGE = (2, 20)

####################################

NUM_CASES = 10

TEST_CASE_FORMAT = """
case = Test %d
input = %d
%d
output = /.*%d.*/
"""

####################################

toh_cnt = 0
toh_k = 1


def TOH(n, src, dst, aux):
    global toh_cnt

    if n == 1:
        if n == toh_k:
            toh_cnt += 1
        # print("Move disk 1 from rod %s to rod %s " % (src, dst))
        return

    TOH(n - 1, src, aux, dst)

    # print("Move disk %d from rod %s to rod %s" % (n, src, dst))
    if n == toh_k:
        toh_cnt += 1

    TOH(n - 1, aux, dst, src)


for i in range(1, 1 + NUM_CASES):

    inp = randint(*RAND_RANGE)
    toh_k = randint(1, inp)

    toh_cnt = 0
    TOH(inp, "A", "B", "C")
    out = toh_cnt

    # out = 2 ** (inp - toh_k)

    print(TEST_CASE_FORMAT % (i, inp, toh_k, out))
