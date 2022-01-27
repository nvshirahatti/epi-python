# O(log n) time | O(1) space
def search_smallest(A):
    left, right = 0, len(A) - 1

    while left < right:
        mid = left + (right - left) // 2
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == "__main__":
    A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
    assert search_smallest(A) == 4
    print("All tests passed!")
