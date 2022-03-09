#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 5:46 下午
# @Author  : xinming
# @File    : 145_postorder_traversal.py

# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root):
            if not root:
                return None
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        res = []
        postorder(root)
        return res

if __name__=='__main__':
    root=TreeNode(val=0)
    root.left=TreeNode(1)
    root.right=TreeNode(2)
    root.left.left=TreeNode(3)
    root.right.right=TreeNode(4)
    out = Solution().postorderTraversal(root)
    print(out)