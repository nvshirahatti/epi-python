from bisect import bisect, bisect_left


def binary_search(A, t):
    left, right = 0, len(A) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] == t:
            return mid
        elif A[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_with_bisect(A, t):
    i = bisect_left(A, t)
    if i != len(A) and A[i] == t:
        return i
    return -1


if __name__ == "__main__":
    A = range(100)
    t = 79
    sln = binary_search(A, t)
    print(sln)
    sln_1 = binary_search_with_bisect(A, t)
    print(sln_1)
