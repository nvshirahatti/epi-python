# O(k) time | O(1) space
def search_kth_smallest_two_sorted_arrays(L1, L2, k):
    sln = []
    i = 0
    p_1 = p_2 = 0
    while i < k:
        if L1[p_1] <= L2[p_2]:
            sln = L1[p_1]
            p_1 -= 1
        else:
            sln = L2[p_2]
            p_2 -= 1
        i += 1
    return sln


if __name__ == "__main__":
    L1 = [2, 3, 6, 7, 9]
    L2 = [1, 4, 8, 10]
    k = 5
    search_kth_smallest_two_sorted_arrays(L1, L2, k)
    assert search_kth_smallest_two_sorted_arrays(L1, L2, k) == 6
    print("All tests passed!")
