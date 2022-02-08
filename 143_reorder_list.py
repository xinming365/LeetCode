#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/7 11:50 上午
# @Author  : xinming
# @File    : 143_reorder_list.py
from ListNode import ListNode, MyLinkedList

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        mid = self.get_middle(head)
        l1=head

        l2 = mid.next
        mid.next = None
        l2 = self.reverse_link(l2)
        out = self.merge_list(l1, l2)
        return out

    def get_middle(self, head):
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow

    def reverse_link(self, head):

        pre = None
        curr = head
        while curr:
            nex = curr.next
            curr.next = pre
            pre = curr
            curr=nex
        # 要保持一致，返回dummy_head
        return pre

    def merge_list(self, l1:ListNode, l2:ListNode):
        while l1 and l2:
            tmp_l1 = l1.next
            tmp_l2 = l2.next

            l1.next = l2
            l1=tmp_l1

            l2.next=l1
            l2 = tmp_l2
        return l1


if __name__=='__main__':
        ll = ListNode(3)
        ll.next=ListNode(2)
        ll.next=ListNode(1)
        ll.next = ListNode(4)
        out = Solution().reorderList(ll)