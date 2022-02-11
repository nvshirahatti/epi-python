from typing import List


# O(m + n) time | O(1) space
def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    i = len(A) - 1
    m -= 1
    n -= 1

    while n >= 0:
        if m >= 0 and A[m] >= B[n]:
            A[i] = A[m]
            m -= 1
        else:
            A[i] = B[n]
            n -= 1
        i -= 1


if __name__ == "__main__":
    A = [5, 13, 17, 0, 0, 0, 0]
    m = 3
    B = [3, 7, 11, 19]
    n = 4
    merge_two_sorted_arrays(A, m, B, n)
    assert A == [3, 5, 7, 11, 13, 17, 19]
    print("All tests passed!")
