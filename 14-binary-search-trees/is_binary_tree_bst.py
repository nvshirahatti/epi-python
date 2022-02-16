# O(n) time | O(h) space (aux) | h: depth/height
def is_binary_tree_bst(root, left, right):
    if not root:
        return True

    if not (root.val < right and root.val > left):
        return False

    return is_binary_tree_bst(root.left, left, root.val) and is_binary_tree_bst(
        root.right, root.val, right
    )
