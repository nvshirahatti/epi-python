# Binary Trees

- Tree: left subtree, rigth subtree
- Binary tree is often binary search tree
- Binary search trees: keys are sorted
- Parent-child relationships on nodes
- Leaf: node with no descendant

- Full binary tree: binary tree; every node has 2 children, except leaves
- Perfect binary tree: full binary tree; all leaves are at same depth
- Complete binary tree: binary tree; every level is filled, except last; all nodes are as far left as possible
- Balanced binary tree: binary tree; left and right subtrees of every node differ by no more than 1

## Traverse

- Inorder: left, root, right
- Preorder: root, left, right
- Postorder: left, right, root

O(n) time | O(h) space | n: nodes, h: height
h -> min: log(n) (balanced), max: n (skewed tree)
