#!/bin/python3

# Tests for: Insert a node at the head of a linked list

import unittest
from solution import SinglyLinkedListNode, SinglyLinkedList, insertNodeAtHead


def linked_list_to_python_list(head):
    """Helper: converts linked list to a Python list for easy assertion."""
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result


class TestInsertNodeAtHead(unittest.TestCase):

    def test_insert_into_empty_list(self):
        result = insertNodeAtHead(None, 1)
        self.assertEqual(linked_list_to_python_list(result), [1])

    def test_new_node_becomes_head(self):
        llist = SinglyLinkedList()
        llist.head = insertNodeAtHead(llist.head, 5)
        llist.head = insertNodeAtHead(llist.head, 10)
        self.assertEqual(llist.head.data, 10)

    def test_previous_head_becomes_second(self):
        llist = SinglyLinkedList()
        llist.head = insertNodeAtHead(llist.head, 5)
        llist.head = insertNodeAtHead(llist.head, 10)
        self.assertEqual(llist.head.next.data, 5)

    def test_insertion_order_reverses_input(self):
        # Inserting [1, 2, 3] one by one at head produces [3, 2, 1]
        llist = SinglyLinkedList()
        for val in [1, 2, 3]:
            llist.head = insertNodeAtHead(llist.head, val)
        self.assertEqual(linked_list_to_python_list(llist.head), [3, 2, 1])

    def test_single_element_list(self):
        llist = SinglyLinkedList()
        llist.head = insertNodeAtHead(llist.head, 42)
        self.assertEqual(linked_list_to_python_list(llist.head), [42])

    def test_tail_next_is_none(self):
        # The last node's next must always be None
        llist = SinglyLinkedList()
        for val in [1, 2, 3]:
            llist.head = insertNodeAtHead(llist.head, val)
        current = llist.head
        while current.next:
            current = current.next
        self.assertIsNone(current.next)


if __name__ == '__main__':
    unittest.main(verbosity=2)
