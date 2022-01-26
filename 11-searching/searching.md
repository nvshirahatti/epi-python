# Searching

- Static data -> array; Dynamic updates -> chapter 10, 12, and 14

## Binary search

```python
def binary_search(t, A):
  L, U = 0, len(A) - 1
  while L <= U:
    M = (L + U) // 2 # potential overflow
    if A[M] < t:
      L = M + 1
    elif A[M] == t:
      return M
    else:
      U = M - 1
  return - 1
```

To avoid overflow, use `M = L + (U - L) // 2` which is equivalent to `M = (2L + U - L) // 2`

- Binary search is O(log n) time, better than O(n), but requires O(n \* log n) time.
- If many searches to perform, sorting is a good investment

- Apply binary search to search an interval if real numbers or integers
- If solution uses sorting and computation after sorting is faster than sorting (O(n) or O(log n)), look for solutitons that do not perform a **complete** sort
- Consider time/space tradeoffs

## Libraries

- `bisect.bisect_left(A, t)`: find first element **greater than or equal** to targeted value. If all elements less than targeted value, return len(A)
- `bisect.bisect_right(A, t)`: find first element **greater** to targeted value. If all elements less than or equal to targetd value, return len(A)
