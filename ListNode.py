#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/2 10:08 上午
# @Author  : xinming
# @File    : ListNode.py

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.dummy_head = ListNode(0)


    def get(self, index: int) -> int:
        """
        Get the value of the i-th node in the linked list.
        :param index:
        :return:
        """
        if index < 0 or index >= self.size:
            return -1

        curr = self.dummy_head
        for i in range(index+1):
            curr = curr.next
        return curr.val

    def print_all(self):
        curr = self.dummy_head
        while curr:
            print(curr.val)
            curr=curr.next


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return None

        # Make it meaningful
        if index < 0:
            index= 0

        self.size+=1 # update the size.

        predecessor = self.dummy_head
        for _ in range(index):
            predecessor = predecessor.next
        to_add = ListNode(val)

        to_add.next = predecessor.next
        predecessor.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        # meaningless if index<0 or larger than the size.
        if index < 0 or index >= self.size:
            return None
        # update the size of linked list.
        self.size -= 1
        predecessor = self.dummy_head
        for _ in range(index):
            predecessor = predecessor.next
        predecessor.next = predecessor.next.next