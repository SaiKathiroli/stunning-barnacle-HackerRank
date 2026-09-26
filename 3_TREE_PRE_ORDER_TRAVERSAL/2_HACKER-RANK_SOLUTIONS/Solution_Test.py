# Problem   : Tree - Preorder Traversal
# Platform  : HackerRank
# URL       : https://www.hackerrank.com/challenges/tree-preorder-traversal
# File      : local_test.py — runs independently, no HackerRank input needed


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def preOrder(root):
    if root is None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


# ── Test Helpers ──────────────────────────────────────────────────────────────

def build_tree(values):
    tree = BinarySearchTree()
    for val in values:
        tree.create(val)
    return tree


def run_test(description, values, expected):
    print(f"Test  : {description}")
    print(f"Input : {values}")
    print(f"Expect: {expected}")
    print(f"Got   : ", end="")
    tree = build_tree(values)
    preOrder(tree.root)
    print("\n")


# ── Test Cases ────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    # Test 1 — Balanced BST
    #
    #         4
    #        / \
    #       2   6
    #      / \ / \
    #     1  3 5  7
    #
    # Preorder: 4 → 2 → 1 → 3 → 6 → 5 → 7
    run_test(
        description="Balanced BST",
        values=[4, 2, 6, 1, 3, 5, 7],
        expected="4 2 1 3 6 5 7"
    )

    # Test 2 — Right-skewed (every node only has a right child)
    #
    #   1
    #    \
    #     2
    #      \
    #       3
    #        \
    #         4
    #
    # Preorder: 1 → 2 → 3 → 4
    run_test(
        description="Right-skewed tree",
        values=[1, 2, 3, 4],
        expected="1 2 3 4"
    )

    # Test 3 — Left-skewed (every node only has a left child)
    #
    #       4
    #      /
    #     3
    #    /
    #   2
    #  /
    # 1
    #
    # Preorder: 4 → 3 → 2 → 1
    run_test(
        description="Left-skewed tree",
        values=[4, 3, 2, 1],
        expected="4 3 2 1"
    )

    # Test 4 — Single node (edge case)
    #
    # Preorder: 42
    run_test(
        description="Single node",
        values=[42],
        expected="42"
    )

    # Test 5 — HackerRank sample input
    #
    #   1
    #    \
    #     2
    #      \
    #       5
    #      / \
    #     3   6
    #      \
    #       4
    #
    # Preorder: 1 → 2 → 5 → 3 → 4 → 6
    run_test(
        description="HackerRank sample input",
        values=[1, 2, 5, 3, 6, 4],
        expected="1 2 5 3 4 6"
    )