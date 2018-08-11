"""Python program for implementation of Selection, Insertion, Bubble Sort"""

from random import randrange

NUM_CASES = 20

TEST_CASE_FORMAT = """
case = Test %d
input = %s
output = "%s"
"""


def selection_sort(A):

    swaps = 0

    # Traverse through all array elements
    n = len(A)
    for i in range(n):

        # Assume this number is minimum
        min_idx = i

        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, n):
            if A[min_idx] > A[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        if min_idx != i:
            A[i], A[min_idx] = A[min_idx], A[i]
            swaps += 1

    return swaps


def bubble_sort(A):

    swaps = 0

    # Traverse through all array elements
    n = len(A)
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swaps += 1

    return swaps


def insertion_other(A):

    # Doesn't use swaps directly. See Wikipedia.

    # Traverse through all array elements (except first)
    for i in range(1, len(A)):

        key = A[i]

        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = key


def insertion_swap(A):

    swaps = 0

    # Traverse through all array elements (except first)
    for i in range(1, len(A)):

        j = i

        # Insert A[i] into list 0..i-1
        while (j > 0 and A[j] < A[j - 1]):
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1

            swaps += 1

    return swaps


def random_list(sz):
    return [randrange(1, 100) for _ in range(sz)]


if __name__ == '__main__':

    # L = [5, 2, 3, 4, 5]

    # L = L[::-1]

    for i in range(1, 1 + NUM_CASES):

        L = random_list(randrange(10, 100))

        # for algorithm in [insertion_swap, selection_sort, bubble_sort]:
        #     print(algorithm.__name__, algorithm(list(L)))

        inp = "[" + "; ".join(map(str, L)) + "]"

        out = bubble_sort(list(L))

        print(TEST_CASE_FORMAT % (i, inp, out))
