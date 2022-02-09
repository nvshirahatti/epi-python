from typing import List


# O(m + n) time | O(1) space | m: len A, n: len B
def intersect_two_sorted_array(A: List[int], B: List[int]) -> List[int]:
    Z = []
    a = b = 0

    while a < len(A) and b < len(B):
        if A[a] == B[b] and A[a] not in Z:
            Z.append(A[a])
            a += 1
            b += 1
        elif A[a] < B[b]:
            a += 1
        else:
            b += 1

    return Z


if __name__ == "__main__":
    A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
    B = [5, 5, 6, 8, 8, 9, 10, 10]
    assert intersect_two_sorted_array(A, B) == [5, 6, 8]
    print("All tests passed!")
