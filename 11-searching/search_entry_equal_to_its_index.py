from typing import List


# O(log n) time | O(1) space
def search_entry_equal_to_its_index(A: List[int]) -> int:
    left, right = 0, len(A) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if mid == A[mid]:
            return mid
        elif mid < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == "__main__":
    A = [-2, 0, 2, 3, 6, 7, 9]
    assert (
        search_entry_equal_to_its_index(A) == 2
        or search_entry_equal_to_its_index(A) == 3
    )
    print("All tests passed!")
