#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/3 12:06 下午
# @Author  : xinming
# @File    : 24_swapPairs.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head
        curr = dummy_head
        while curr.next and curr.next.next:
            start = curr.next
            end = curr.next.next
            curr.next = end # 0->2
            start.next = end.next # 1->3
            end.next = start
            curr = start
        return dummy_head.next

