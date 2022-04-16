#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/6 12:01 上午
# @Author  : xinming
# @File    : 572_is_subtree.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution2:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        if (not root) or (not subRoot):
            return False
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if (not root) or (not subRoot):
            return False
        return root.val==subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)





