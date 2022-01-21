from binary_tree_node import BinaryTreeNode


# O(n) time | O(h) space | n: nodes, h: height/depth
def is_symmetric(tree):
    def check_symmetric(first_subtree, second_subtree):
        if not first_subtree and not second_subtree:
            return True
        elif first_subtree and second_subtree:
            return (
                first_subtree.data == second_subtree.data
                and check_symmetric(first_subtree.left, second_subtree.right)
                and check_symmetric(first_subtree.right, second_subtree.left)
            )
        else:
            return False

    return not tree or check_symmetric(tree.left, tree.right)


if __name__ == "__main__":
    # Test One
    three_one = BinaryTreeNode(3)
    three_two = BinaryTreeNode(3)
    two_one = BinaryTreeNode(2, None, three_one)
    two_second = BinaryTreeNode(2, three_two, None)
    six_one = BinaryTreeNode(6, None, two_one)
    six_two = BinaryTreeNode(6, two_second, None)
    three_one_four = BinaryTreeNode(314, six_one, six_two)

    assert is_symmetric(three_one_four) is True

    # Test Two
    three = BinaryTreeNode(3)
    five_six_one_1 = BinaryTreeNode(561, None, three)
    five_six_two_2 = BinaryTreeNode(561)
    six_1 = BinaryTreeNode(6, None, five_six_one_1)
    six_2 = BinaryTreeNode(6, five_six_two_2, None)
    three_one_four_2 = BinaryTreeNode(314, six_1, six_2)

    assert is_symmetric(three_one_four_2) is False

    print("All tests passed!")
