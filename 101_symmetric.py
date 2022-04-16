#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/14 9:58 下午
# @Author  : xinming
# @File    : 101_symmetric.py
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(left, right):
            if (not left) and (not right):
                return True
            if (not left) or (not right):
                return False
            return left.val==right.val and dfs(left.right, right.left) and dfs(left.left, right.right)


if __name__=='__main__':
    Solution().isSymmetric()