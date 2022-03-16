def n_queens(n):
    col = set()
    pos_diag = set()  # r + c
    neg_diag = set()  # r - c
    board = [["."] * n for _ in range(n)]
    res = []

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])

        for c in range(n):
            if c in col and r + c in pos_diag and r - c in neg_diag:
                continue

            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res


if __name__ == "__main__":
    n = 4
    res = n_queens(n)
    print(res)
