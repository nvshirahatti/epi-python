# O(s*n) time | O(n) space | s: points, n: final score
def num_combinations_for_final_score(points, final_score):
    board = [1] + [0] * final_score

    for point in points:
        for i in range(point, final_score + 1):
            board[i] += board[i - point]

    return board[-1]


if __name__ == "__main__":
    assert num_combinations_for_final_score([2, 3, 7], 12) == 4
    assert num_combinations_for_final_score([3, 5, 10], 20) == 4
    assert num_combinations_for_final_score([3, 5, 10], 13) == 2
    print("All tests passed!")
