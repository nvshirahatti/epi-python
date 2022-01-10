from list_node import ListNode


# O(n) time | O(1) space
def reverse_sublist(L: list, start: int, finish: int):
    # Before: 11 -> 3 -> 5 -> 7 -> 2
    #         0     1    2    3    4
    # After:  11 -> 7 -> 5 -> 3 -> 2
    dummy_head = sublist_head = ListNode(0, L)

    # Go to start index
    for _ in range(1, start):  # because of position (not index)
        sublist_head = sublist_head.next

    # sublist_head = 11; sublist_iter = 3; temp = 5; temp.next = 7
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next


if __name__ == "__main__":
    L = ListNode.from_list([11, 3, 5, 7, 2])
    print(f"Before: {L}")
    start = 2  # 2th position (not index)
    finish = 4  # 4th position (not index)
    print(f"After:  {reverse_sublist(L, start, finish)}")
