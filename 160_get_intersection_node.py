#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/30 10:30 上午
# @Author  : xinming
# @File    : 160_get_intersection_node.py


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha=headA
        known=set()
        while ha:
            known.add(ha)
            ha=ha.next
        hb = headB
        while hb:
            if hb in known:
                return headB
            headB = headB.next
        return None
