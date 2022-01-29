#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/28 8:15 上午
# @Author  : xinming
# @File    : 2_add_two_numbers.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def init_list_node(l):
    length = len(l)
    curr = node = ListNode()
    for i in range(length):
        # next = l[i+1] if i< length else None
        node.next = ListNode(val=l[i])
        node = node.next #
    return curr.next

def initList(self, data):
    # 创建头结点
    self.head = ListNode(data[0])
    r = self.head
    p = self.head
    # 逐个为 data 内的数据创建结点, 建立链表
    for i in data[1:]:
        node = ListNode(i)
        p.next = node
        p = p.next
    return r

def print_nodes(n):
    print(n.val)
    while n!=None:
        print(n.val)
        n=n.next



class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = 0
        # 两者地址要求相同，curr保存当前步地址，res才能保存一系列链表。
        out = curr = ListNode()
        # 非空满足循环条件
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            res = x+y+add
            add = res//10
            curr.next = ListNode(val = res%10)
            curr = curr.next  # 覆盖掉当前地址
            # 防止某一链表已经为空，空链表.next会报错
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if add:
            curr.next = ListNode(add)
        return out.next



if __name__=='__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]
    ll1= init_list_node(l1)
    ll2 = init_list_node(l2)
    # print_nodes(out.next.val)
    out = Solution().addTwoNumbers(ll1, ll2)
    print_nodes(out)
