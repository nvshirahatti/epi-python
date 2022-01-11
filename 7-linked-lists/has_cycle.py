from list_node import ListNode


# Tortoise and hare / Floyd's cycle detection algorithm
# O(n) time | O(1) space
def has_cycle(head):
    slow = fast = head

    # This condition covers an edge case when fast has
    # no next node or next.next node
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next

        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow

    return None


if __name__ == "__main__":
    # 0 -> 1 -> 2 -> 3
    #           ↑    ↓
    #           5 <- 4
    entry = ListNode(2)
    entry.next = ListNode(3, ListNode(4, ListNode(5, entry)))
    head = ListNode(0, ListNode(1, entry))
    sln = has_cycle(head)
    print(f"Entry of cycle: {sln.data if sln else 'None'}")
