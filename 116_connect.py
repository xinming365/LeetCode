#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 4:57 下午
# @Author  : xinming
# @File    : 116_connect.py

"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from typing import Optional
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = [root]

        while queue:
            size = len(queue)
            tmp = queue[0]
            for i in range(1, size):
                tmp.next = queue[i]
                tmp = queue[i]
            for i in range(size):
                tmp = queue.pop(0)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
        return root


if __name__=='__main__':
    root = Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    out = Solution().connect(root)