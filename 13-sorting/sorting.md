# Chapter 13. Sorting

- O(nlogn): heapsort, merge sort, and quicksort
- Heapsort: in-place, but **not** stable
- Mergesort: stable, but **not** in-place
- Quicksort: O(n^2) worst case
- A well-implemented quicksort is usually the best choice for sorting

Alternatives:

- Short arrays (< 10 elements): insertion sort
- If every elemetns is known to be at **most k places** from sorted, use min-heap O(nlogk)
- If small number of distinct keys, e.g. integers in range [0..255], counting sort

Sorting problems:

1. Use sorting to make subsequent steps in an algorithm **simpler**: use library sort function, possibly with a custom comparator
2. Design a custom sorting routine: use data structure like BST, heap, or array indexed by value

- If inputs have naterual ordering, sorting can be used as a preprocessing step to speed up searching
- For specialized input, a very small range of values, or a small number of values, it's possible to sort in O(n) time rather than O(nlogn) time
- Sorting can be implemented in **less space** than required by a brute-force approach
- Sometimes it is not obvious what to sort on, should a collection of intervals be sorted on starting points or endpoints?

## Libraries

- sort() is in-place
- sorted() is to sort an iterable

- `sort()` implements a stable in-place sort, returns None, takes 2 arguments`key=None` and `reverse-False`
- `sorted()` takes an iterable and returns a new list, also take 2 arguments like `sort()`
