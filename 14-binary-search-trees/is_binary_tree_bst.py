from bstnode import BSTNode

# O(n) time | O(h) space (aux) | h: depth/height
def is_binary_tree_bst(
    root: type[BSTNode], low_range=float("-inf"), high_range=float("inf")
) -> bool:
    if not root:
        return True

    if not (root.val < high_range and root.val > low_range):
        return False

    return is_binary_tree_bst(root.left, low_range, root.val) and is_binary_tree_bst(
        root.right, root.val, high_range
    )
