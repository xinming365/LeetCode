#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/27 10:42 下午
# @Author  : xinming
# @File    : 19_remove_nth_from_end.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def get_length(head):
            cur = head
            l = 0
            while cur!=None:
                l+=1
                cur = cur.next
            return l
        L = get_length(head)
        dummy = ListNode(0)
        dummy.next=head
        curr = dummy
        for _ in range(1, L-n+1):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next

if __name__=='__main__':

    out = Solution().removeNthFromEnd(head, 2)