from heapq import merge
import heapq


# O(n*logk) time | O(n) space
def sort_k_increasing_decreasing_array(A: list[int]) -> list[int]:
    sorted_subarrays = []
    INCREASING, DECREASING = range(2)
    subarray_type = INCREASING
    start_idx = 0

    for i in range(1, len(A) + 1):
        if (
            i == len(A)
            or (A[i - 1] < A[i] and subarray_type == DECREASING)
            or (A[i - 1] >= A[i] and subarray_type == INCREASING)
        ):
            sorted_subarrays.append(
                A[start_idx:i]
                if subarray_type == INCREASING
                else A[i - 1 : start_idx - 1 : -1]
            )
            start_idx = i
            subarray_type = DECREASING if subarray_type == INCREASING else INCREASING
    return list(heapq.merge(*sorted_subarrays))


if __name__ == "__main__":
    A = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]  # -> k = 4 inc-dec-inc-dec
    sln = sort_k_increasing_decreasing_array(A)
    assert sln == [57, 131, 190, 221, 294, 339, 418, 442, 452, 493]
    print("All tested passed!")
