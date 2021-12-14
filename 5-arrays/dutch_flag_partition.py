# O(n) time | O(1) space
def dutch_flag_partition(pivot_index, A):
    # 0 1 2 0 2 1 1
    p = A[pivot_index]
    i = 0
    r = len(A) - 1

    while i <= r:
        if A[i] >= p:
            A[r], A[i] = A[i], A[r]
            r -= 1
            continue
        i += 1


if __name__ == "__main__":
    A = [0, 1, 2, 0, 2, 1, 1]
    dutch_flag_partition(2, A)
    print(A)
