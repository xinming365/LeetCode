#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/30 11:57 上午
# @Author  : xinming
# @File    : 82_delete_duplicate.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


if __name__=='__main__':
    pass