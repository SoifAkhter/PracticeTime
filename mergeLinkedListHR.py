#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    if  not head1:
        return head2
    elif not head2:
        return head1
    else:
        if head1.data < head2.data:
            temp = SinglyLinkedListNode(head1.data)
            res = temp
            head1 = head1.next
        else:
            temp = SinglyLinkedListNode(head2.data)
            res = temp
            head2= head2.next

        while head1 or head2:
            if not head1:
                temp.next = head2
                return res
            elif not head2:
                temp.next = head1
                return res
            else:
                if head1.data <= head2.data:
                    temp.next = SinglyLinkedListNode(head1.data)
                    head1 = head1.next
                elif head1.data > head2.data:
                    temp.next = SinglyLinkedListNode(head2.data)
                    head2 = head2.next
                temp = temp.next
        return res




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
