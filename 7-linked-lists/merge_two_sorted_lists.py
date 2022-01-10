from list_node import ListNode


# O(m + n) time | O(1) space
# m: L1 length; n: L2 length
def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2

    return dummy_head.next


if __name__ == "__main__":
    L1 = ListNode.from_list([2, 5, 7])
    L2 = ListNode.from_list([3, 11])
    sln = merge_two_sorted_lists(L1, L2)
    print(sln)
