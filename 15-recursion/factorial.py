# O(n) time | O(n) space
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    assert factorial(3) == 6
    print("All tests passed!")
