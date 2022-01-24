# I am unable to understand this problem for now
# Definitely a hard question https://leetcode.com/problems/n-queens/
def n_queens(n):
    def solve_n_queens(row):
        if row == n:
            result.append(
                list(col_placement)
            )  # to create a copy of list to append, instead pass ref
            return

        for col in range(n):
            if all(
                abs(c - col) not in (0, row - i)
                for i, c in enumerate(col_placement[:row])
            ):
                col_placement[row] = col
                solve_n_queens(row + 1)

    result, col_placement = [], [0] * n
    solve_n_queens(0)
    return result


if __name__ == "__main__":
    n = 4
    sln = n_queens(n)
    print(sln)
