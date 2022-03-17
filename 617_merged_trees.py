#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 11:29 下午
# @Author  : xinming
# @File    : 617_merged_trees.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        def dfs_merge(t1, t2):
            if not t1:
                return t2
            if not t2:
                return t1

            merged = TreeNode(t1.val + t2.val)

            merged.left = dfs_merge(t1.left, t2.left)
            merged.right = dfs_merge(t1.right, t2.right)
            return merged

        return dfs_merge(root1, root2)



if __name__=='__main__':
    pass

    # Solution().mergeTrees(t1, t2)