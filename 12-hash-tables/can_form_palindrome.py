import collections


# O(n) time | O(c) space | n: string length, c: distinct characters
def can_form_palindrome(s: str) -> bool:
    # A string can be permuted to form a palindrome if and only if the number of chars
    # whose frequencies is odd is at most 1
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


if __name__ == "__main__":
    s = "edified"
    can_form_palindrome(s)
    assert can_form_palindrome(s) == True
    print("All tests passed!")
