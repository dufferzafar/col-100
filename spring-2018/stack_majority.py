import numpy as np

from random import randrange

NUM_CASES = 25

TEST_CASE_FORMAT = """
case = Test %d
input = %s
output = "%s"
"""

if __name__ == '__main__':

    for i in range(1, 1 + NUM_CASES):

        L = np.random.randint(2, size=randrange(25, 50))

        inp = "[" + "; ".join(map(str, L)) + "]"

        out = np.bincount(L).argmax()

        print(TEST_CASE_FORMAT % (i, inp, out))
