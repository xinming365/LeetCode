#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/13 4:27 下午
# @Author  : xinming
# @File    : 173_bst_iterator.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack=[]
        while root:
            self.stack.append(root)
            root = root.left


    def next(self) -> int:
        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node=node.left
        return cur.val

    def hasNext(self) -> bool:
        if len(self.stack)>0:
            return True
        else:
            return False