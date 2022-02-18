from collections import deque
from bstnode import BSTNode


# O(h + k) time | O(h + k) space (aux + mem)
def find_k_largest_in_bst(root: type[BSTNode], k: int) -> type[BSTNode]:
    def ask_helper(node):
        if node and len(k_largest_elements) < k:
            ask_helper(node.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(node.data)
                ask_helper(node.left)

    k_largest_elements = []
    ask_helper(root)
    return k_largest_elements
