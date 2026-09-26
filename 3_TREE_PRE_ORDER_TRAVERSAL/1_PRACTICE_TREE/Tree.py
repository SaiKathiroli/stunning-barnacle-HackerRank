"""
        10          ← Root (the top, has no parent)
       /  \
      5    20       ← Children of 10
     / \
    3   7           ← Children of 5; also Leaves (no children of their own)
"""


def create_left_child(parent_node, child_node):
    parent_node.left = child_node
    return child_node


def create_right_child(parent_node, child_node):
    parent_node.right = child_node
    return child_node


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def pre_order_traversal(root: Node):
    if root is None:
        return
    print(root.value)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)


if __name__ == "__main__":
    parent_root = Node(10)
    left = create_left_child(parent_root, Node(5))
    right = create_right_child(parent_root, Node(20))
    create_left_child(left, Node(3))
    create_right_child(left, Node(7))
    """
            10          ← Root (the top, has no parent)
           /  \
          5    20       ← Children of 10
         / \
        3   7           ← Children of 5; also Leaves (no children of their own)
    """
    pre_order_traversal(parent_root)

