def search_bst(tree, key):
    return (
        tree
        if not tree or tree.data == key
        else search_bst(tree.left, key)
        if key < tree.data
        else search_bst(tree.right, key)
    )
