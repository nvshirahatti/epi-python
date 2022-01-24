from itertools import islice
import heapq


def top_k(k, stream):
    min_heap = [(len(s), s) for s in islice(stream, k)]
    heapq.heapify(min_heap)
    for next_string in stream:
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    return [p[1] for p in heapq.nsmallest(k, min_heap)]


if __name__ == "__main__":
    top_k(k, stream)
