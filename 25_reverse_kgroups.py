#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/4 11:52 上午
# @Author  : xinming
# @File    : 25_reverse_kgroups.py
from ListNode import ListNode
from typing import Optional
class Solution:
    def reverse_linked_list(self,head, tail):
        pre = None
        curr = head
        while curr:
            nex  = curr.next
            curr.next = pre
            pre=curr
            curr=nex
        return tail, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre  # 类似于dummy head初始化
            # 找到k组的tail
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse_linked_list(head, tail)

            # 子链表重新接
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return hair.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next


if __name__ == '__main__':
    Solution.reverseKGroup(head, 2)

