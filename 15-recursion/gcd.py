# O(n) time | O(n) space | n: bits to represent input
def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


if __name__ == "__main__":
    x = 156
    y = 36
    assert gcd(x, y) == 12
    print("All tests passed!")
