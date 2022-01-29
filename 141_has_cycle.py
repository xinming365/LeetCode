#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/29 10:56 下午
# @Author  : xinming
# @File    : 141_has_cycle.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        known=set()
        while head:
            if head in known:
                return True
            known.add(head)
            head = head.next
        return False


class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 如果相遇
            if slow == fast:
                p = head
                q = slow
                while p!=q:
                    p = p.next
                    q = q.next
                #你也可以return q
                return p

        return None



if __name__=='__main__':
    # Solution.hasCycle()
    pass