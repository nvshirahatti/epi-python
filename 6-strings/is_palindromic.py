# O(n) time | O(1) space
# Note: O(1) space because it is a for-loop, not a list comprehension
def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))


if __name__ == "__main__":
    # s = "aaron"
    s = "racecar"
    print(f"{s} -> {is_palindromic(s)}")
