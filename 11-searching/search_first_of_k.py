import bisect


# O(log n) time | O(1) space
def search_first_of_k(A, k):
    left, right, sln = 0, len(A) - 1, -1
    while left <= right:
        mid = left + (right - left) // 2

        if A[mid] == k:
            sln = mid
            right -= 1
        elif A[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return sln


def search_last_of_k(A, k):
    left, right, sln = 0, len(A) - 1, -1
    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] == k:
            sln = mid
            left += 1
        elif A[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return sln


# O(log n) time | O(1) space
def search_first_of_k_with_bisect(A, k):
    i = bisect.bisect_left(A, k)
    if i != len(A) and A[i] == k:
        return i
    return -1


if __name__ == "__main__":
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    assert search_first_of_k(A, 108) == 3
    assert search_first_of_k(A, 285) == 6
    assert search_first_of_k_with_bisect(A, 108) == 3
    assert search_first_of_k_with_bisect(A, 285) == 6
    assert search_last_of_k(A, 108) == 4
    assert search_last_of_k(A, 285) == 8
    print("All tests passed!")
