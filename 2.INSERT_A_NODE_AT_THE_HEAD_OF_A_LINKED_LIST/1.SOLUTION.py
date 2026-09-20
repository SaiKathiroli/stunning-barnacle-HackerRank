#!/bin/python3

# HackerRank - Data Structures / Linked Lists
# Problem  : Insert a node at the head of a linked list
# URL      : https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list

import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)


def insertNodeAtHead(llist, data):
    new_head_node = SinglyLinkedListNode(data)
    new_head_node.next = llist
    return new_head_node


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', sys.stdout)
    print()
