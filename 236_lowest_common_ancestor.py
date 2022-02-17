#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/14 3:24 下午
# @Author  : xinming
# @File    : 236_lowest_common_ancestor.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 递归。root为空，或者找到p或者q的时候返回root，不为空。
        if not root or root == p or root == q:
            return root
        # 左边，右边递归遍历
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 左右同时为空 不满足 返回上一层。
        if not left and not right:
            return # 1.
        # 右边不空，返回右边
        if not left:
            return right # 3.
        # 左边不空，返回左边
        if not right:
            return left # 4.
        # 左右两边都不空，是最近公共祖先节点
        return root # 2. if left and right:

if __name__=='__main__':
    root = TreeNode(3)
    root.left=TreeNode(5)
    root.left.left=TreeNode(6)
    root.left.right=TreeNode(2)
    root.left.right.left=TreeNode(7)
    root.left.right.right=TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    p = TreeNode(7)
    q = TreeNode(4)
    ans = Solution().lowestCommonAncestor(root, p, q)
    print(ans)
