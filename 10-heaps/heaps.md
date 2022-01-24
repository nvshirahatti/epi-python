# Heaps

- Heap is complete and specialized binary tree
- Keys must satisfy _heap property_ - key each node is at least equal to keys stored at its children
- Max-heap is implemented as array. Node (idx i) is ancestor (parent) of nodes at 2i + 1 and 2i + 2
- O(log n) insertion, O(1) max lookup, O(log n) max delete
- Priority queue = heap
- Min-heap is same with min equivalency
- Heap is used when all you care about is largest and smallest; do not need to support fast lookup, delete, or search operations
- To compute k largest, use min-heap; to compute k smallest, use max-heap

- heapq library:
  - heapq.heapify(L)
  - heapq.nlargest(k, L) / heapq.nsmallest(k, L)
  - heapq.heappush(h, e) -> push e
  - heapq.heappop(h) -> pop smallest
  - heapq.heappushpop(h, a) -> push a, pop smallest
  - e = h[0] -> smallest element
- heapq provides min-heap; to use max-heap, insert negative
