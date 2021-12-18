# O(n) time | O(n) space ?
def is_palindromic(s):
    return all([s[i] == s[~i] for i in range(len(s) // 2)])


if __name__ == "__main__":
    # s = "aaron"
    s = "racecar"
    print(is_palindromic(s))
