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

    @classmethod
    def from_list(cls, L: list) -> "ListNode":
        next_node = None
        for i in L[::-1]:
            current_node = ListNode(i, next_node)
            next_node = current_node
        return next_node
