# O(n*m) time | O(n + m) space
def multiply(A, B):
    sign = -1 if (A[0] < 0) ^ (B[0] < 0) else 1

    A[0], B[0] = abs(A[0]), abs(B[0])

    solution = [0] * (len(A) + len(B))

    for i in range(len(A))[::-1]:
        for j in range(len(B))[::-1]:
            solution[i + j + 1] += A[i] * B[j]
            solution[i + j] += solution[i + j + 1] // 10
            solution[i + j + 1] %= 10

    while solution[0] == 0:
        del solution[0]

    solution[0] = solution[0] * sign

    return solution


if __name__ == "__main__":
    A = [-1, 2, 4]
    B = [3, 5]
    print(multiply(A, B))
