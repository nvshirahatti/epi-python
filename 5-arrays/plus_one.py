# O(n) time | O(1) space
def plus_one(A):
    A.reverse()
    A[0], carry = (A[0] + 1) % 10, (A[0] + 1) // 10

    for i in range(1, len(A)):
        if carry:
            A[i], carry = (A[i] + carry) % 10, (A[i] + carry) // 10
    if carry:
        A.append(carry)

    A.reverse()


def plus_one_2(A):
    A[-1] += 1

    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)


if __name__ == "__main__":
    A = [9, 8]
    plus_one_2(A)
    print(A)
