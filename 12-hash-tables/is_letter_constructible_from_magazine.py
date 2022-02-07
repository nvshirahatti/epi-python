from collections import Counter


# O(m + n) time | O(1) space
# m: len letter_text, n: len magazine_text
# O(1) space because alphabet has limited characters. ASCII: 256 characters
def is_letter_constructible_from_magazine(letter_text: str, magazine_text: str) -> bool:
    return not (Counter(letter_text) - Counter(magazine_text))


if __name__ == "__main__":
    letter_text = "aa"
    magazine_text = "aab"
    is_letter_constructible_from_magazine(letter_text, magazine_text)
    assert is_letter_constructible_from_magazine(letter_text, magazine_text) == True
    print("All tests passed!")
