import heapq
from itertools import islice
from heapq import *

# O(n*logk) time | O(n) space | n: elements, k
# Note: This solution from EPI use O(n) space because of solution array.
# This can be optimized up to O(k) using sliding window to sort in-place
def sort_approximately_sorted_array(L, k):
    sln = []
    min_heap = []

    for i in L[:k]:
        heappush(min_heap, i)

    for i in L[k:]:
        smallest = heappushpop(min_heap, i)
        sln.append(smallest)

    while min_heap:
        smallest = heappop(min_heap)
        sln.append(smallest)

    return sln


if __name__ == "__main__":
    A = [3, -1, 2, 6, 4, 5, 8]
    B = [-1, 2, 3, 4, 5, 6, 8]
    assert sort_approximately_sorted_array(A, 2) == B
    print("All test passed!")
