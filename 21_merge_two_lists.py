#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/27 11:58 下午
# @Author  : xinming
# @File    : 21_merge_two_lists.py
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        head = ListNode(0)
        nl = head
        while l1 and l2:
            if l1.val > l2.val:
                nl.next = l2
                l2 = l2.next
            else:
                nl.next=l1
                l1 = l1.next
            nl = nl.next

        if l1:
            nl.next = l1
        else:
            nl.next = l2
        return head.next
if __name__=='__main__':
    pass
