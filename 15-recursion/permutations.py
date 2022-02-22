# O(n * n!) time | O(n!) space
def permutations(A):
    def solve_permutations(i):
        if i == len(A) - 1:
            R.append(A.copy())
            return None

        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            solve_permutations(i + 1)
            A[i], A[j] = A[j], A[i]

    R = []
    solve_permutations(0)
    return R


if __name__ == "__main__":
    A = [2, 3, 5, 7]
    permutations(A)
    assert permutations(A) == []
    print("All tests passed!")
