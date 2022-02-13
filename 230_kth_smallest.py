#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/13 3:40 下午
# @Author  : xinming
# @File    : 230_kth_smallest.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            # 使用根节点的右节点的最小子节点(在左边)，优先替换。
            root = stack.pop()
            k = k-1
            if k==0:
                return root.val
            root = root.right


if __name__=='__main__':
    root = TreeNode(3)
    root.left=TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(23)
    ans = Solution().kthSmallest(root, 3)
    print(ans)