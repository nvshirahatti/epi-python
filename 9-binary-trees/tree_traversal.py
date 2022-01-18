from binary_tree_node import BinaryTreeNode


# O(n) time | O(h) space | n: nodes, h: height
# h -> min: log(n) (balanced), max: n (skewed tree)
def tree_traversal(root):
    if root:
        # Preorder: root, left, right
        print(f"Preorder: {root.data}")
        tree_traversal(root.left)

        # Inorder: left, root, right
        print(f"Inorder: {root.data}")
        tree_traversal(root.right)

        # Postorder: left, right, root
        print(f"Postorder: {root.data}")


if __name__ == "__main__":
    left = BinaryTreeNode(1)
    right = BinaryTreeNode(2)
    root = BinaryTreeNode(0, left, right)
    tree_traversal(root)
