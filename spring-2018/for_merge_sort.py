from random import randrange

NUM_CASES = 20

TEST_CASE_FORMAT = """
case = Test %d
input = %s
output = "%s"
"""


def random_list(sz, max_):
    return [randrange(1, max_) for _ in range(sz)]


if __name__ == '__main__':

    for i in range(1, 1 + NUM_CASES):

        if 0 <= i <= 5:
            sz = 100
        elif 6 <= i <= 12:
            sz = 10000
        elif 13 <= i <= 20:
            sz = 100000

        L = random_list(sz, 100)

        inp = "[" + "; ".join(map(str, L)) + "]"

        print(TEST_CASE_FORMAT % (i, inp, ""))
