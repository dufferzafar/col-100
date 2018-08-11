from random import randrange

NUM_CASES = 50

TEST_CASE_FORMAT = """
case = Test %d
input = %s
output = "%s"
"""


def chopstick_pairs(d, l):

    n = len(l)

    l.sort()

    pairs = 0
    i = 0
    while i < n - 1:
        if l[i + 1] - l[i] <= d:
            pairs += 1
            i = i + 2
        else:
            i += 1

    return pairs


def random_list(sz):
    return [randrange(1, 10000) for _ in range(sz)]


if __name__ == '__main__':

    # L = [5, 2, 3, 4, 5]
    # L = [1, 3, 3, 9, 4]

    # L = L[::-1]

    # 1 ≤ N ≤ 100,000 (10 5 )
    # 0 ≤ D ≤ 1,000,000,000 (10 9 )
    # 1 ≤ L[i] ≤ 1,000,000,000 (10 9 ) for all integers i from 1 to N

    for i in range(1, 1 + NUM_CASES):

        L = random_list(randrange(10, 100))
        d = randrange(1, 500)
        # d = 1

        inp = str(d) + "\n"
        inp += "[" + "; ".join(map(str, L)) + "]"

        out = chopstick_pairs(d, L)

        print(TEST_CASE_FORMAT % (i, inp, out))
