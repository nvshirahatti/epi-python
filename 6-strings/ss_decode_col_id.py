# O(n) time | O(logn) space
# https://leetcode.com/problems/excel-sheet-column-title/discuss/1473821/Python-Easy-to-Understand-Solution
def ss_decode_col_id(col):
    sln = []

    while col > 0:
        col -= 1
        sln.append(chr(ord("A") + col % 26))
        col //= 26

    return "".join(sln[::-1])


if __name__ == "__main__":
    col = 702
    print(ss_decode_col_id(col))
