from collections import namedtuple


def lca(tree, first_node, second_node):
    Status = namedtuple("Status", ("number_target_nodes", "ancestor"))

    def lca_helper(tree, first_node, second_node):
        if not tree:
            return Status(0, None)

        left_result = lca_helper(tree.left, first_node, second_node)
        if left_result.number_target_nodes == 2:
            return left_result
        right_result = lca_helper(tree.right, first_node, second_node)
        if right_result.number_target_nodes == 2:
            return right_result

        number_target_nodes = (
            left_result.number_target_nodes
            + right_result.number_target_nodes
            + int(tree is first_node)
            + int(tree is second_node)
        )
        return Status(number_target_nodes, tree if number_target_nodes == 2 else None)

    return lca_helper(tree, first_node, second_node).ancestor


if __name__ == "__main__":
    lca()
