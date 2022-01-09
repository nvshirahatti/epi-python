# O(m + n) time | O(1) space
# m: L1 length; n: L2 length


class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self) -> str:
        sln = []
        while self:
            sln.append(str(self.data))
            self = self.next

        return " -> ".join(sln)


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
    L1 = ListNode(2, ListNode(5, ListNode(7)))
    L2 = ListNode(3, ListNode(11))
    sln = merge_two_sorted_lists(L1, L2)
    print(sln)
