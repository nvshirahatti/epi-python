from binary_tree_node import BinaryTreeNode


# 9.1
# O(n) time | O(h) space | n: nodes, h: height/depth
def is_balanced_binary_tree(tree):
    def check_balanced(tree):
        if not tree:
            return (True, -1)

        left = check_balanced(tree.left)
        if not left[0]:
            return (False, 0)

        right = check_balanced(tree.right)
        if not right[0]:
            return (False, 0)

        balanced = abs(left[1] - right[1]) <= 1
        height = max(left[1], right[1]) + 1

        return (balanced, height)

    return check_balanced(tree)[0]


if __name__ == "__main__":
    nine = BinaryTreeNode(9)
    fifteen = BinaryTreeNode(5)
    seven = BinaryTreeNode(7)
    twenty = BinaryTreeNode(20, fifteen, seven)
    three = BinaryTreeNode(3, nine, twenty)

    tree = three
    assert is_balanced_binary_tree(tree) is True

    print("All tests passed!")
