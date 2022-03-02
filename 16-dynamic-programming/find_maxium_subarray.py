import itertools

# LC 53 -> incorrect solution
def find_maximum_subarray(A):
    min_sum, max_sum = 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum


# LC 53 -> correct solution
# O(n) time | O(1) space
def find_maximum_subarray(N):
    cur_sum, max_sum = float("-inf")
    for n in N:
        cur_sum = max(cur_sum + n, n)
        max_sum = max(max_sum, cur_sum)
    return max_sum
