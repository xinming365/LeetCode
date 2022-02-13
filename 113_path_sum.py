#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/13 11:17 上午
# @Author  : xinming
# @File    : 113_path_sum.py


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
from typing import Optional
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(node, target):

            if not node:
                return None
            path.append(node.val)
            target = target - node.val
            if target==0 and not node.left and not node.right:
                res.append(path[:])
            dfs(node.left, target)
            dfs(node.right, target)
            path.pop()
        dfs(root, targetSum)
        return res

if __name__=='__main__':
    root = TreeNode(3)
    root.left=TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    ans = Solution().pathSum(root, 12)
    print(ans)