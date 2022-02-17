from bstnode import BSTNode

# O(h) time | O(1) space | h: height/depth, if tree is balanced h = logn
def find_first_greater_than_k(root: type[BSTNode], k: int) -> type[BSTNode]:
    node = root
    first_so_far = None
    while node:
        if node.data > k:
            node = node.left
            first_so_far = node
        else:
            node = node.right
    return first_so_far
