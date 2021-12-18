# O(n) time | O(n) space; n: number of digits
def int_to_string(x):
    sign = -1 if x < 0 else 1
    x = abs(x)

    s = []

    while x != 0:
        s.append(chr(ord("0") + x % 10))
        x //= 10

    return ("-" if sign == -1 else "") + "".join(s[::-1])


if __name__ == "__main__":
    x = -314
    s = int_to_string(x)
    print(f"{s} ({type(s).__name__})")
