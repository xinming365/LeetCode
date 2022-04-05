#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 11:33 下午
# @Author  : xinming
# @File    : 117_connect.py

"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') :
        if not root:
            return None
        queue = [root]
        while queue:
            n = len(queue)
            tail = None
            for i in range(n):
                curr = queue.pop(0)
                if tail:
                    tail.next = curr
                tail = curr
                left = curr.left
                right = curr.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
        return root

