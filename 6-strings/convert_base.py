# O(n) time | O(n) space
def convert_base(s, b1, b2):
    x = 0

    for i, e in enumerate(s[::-1]):
        # i: 0 1 2
        # e: 5 1 6
        x += int(e) * b1 ** i

    sln = []

    while x != 0:
        # https://stackoverflow.com/questions/16414559/how-to-use-hex-without-0x-in-python
        sln.append(format(x % b2, "X"))
        x //= b2

    return "".join(sln[::-1])


if __name__ == "__main__":
    s = "615"
    b1 = 7
    b2 = 13
    print(convert_base(s, b1, b2))
