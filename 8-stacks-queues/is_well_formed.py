# O(n) time | O(n) space
def is_well_formed(s):
    L = []
    D = {"(": ")", "[": "]", "{": "}"}

    for c in s:
        if c in D:
            L.append(c)
        elif not L or D[L.pop()] != c:
            return False

    return not L


if __name__ == "__main__":
    assert is_well_formed("()(())") is True
    assert is_well_formed("[()[]{()()}]") is True
    assert is_well_formed("[()[]{()()") is False
    print("All tests passed!")
