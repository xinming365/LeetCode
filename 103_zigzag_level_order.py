#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/12 3:25 下午
# @Author  : xinming
# @File    : 103_zigzag_level_order.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        level = 0
        ans = []
        stack = [root]
        while stack:
            curr_ans = []
            level+=1 # 记录二叉树层数
            for _ in range(len(stack)):
                node = stack.pop(0)
                curr_ans.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if level%2==0:
                curr_ans.reverse()
            ans.append(curr_ans)

# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#
#         if root == None:
#             return []
#
#         ans = []
#         stack = []
#         stack.append(root)
#         Layer = 0
#
#         while stack:
#             cur_ans = []
#             Layer += 1
#             lenThisLayer = len(stack)
#             for _ in range(lenThisLayer):
#                 cur_node = stack.pop(0)
#                 cur_ans.append(cur_node.val)
#                 if cur_node.left:
#                     stack.append(cur_node.left)
#                 if cur_node.right:
#                     stack.append(cur_node.right)
#             if Layer % 2 == 0: # 奇数层时倒序数组
#                 cur_ans.reverse()
#             ans.append(cur_ans)
#
#         return ans

if __name__=='__main__':
    root = TreeNode(3)
    root.left=TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    ans = Solution().zigzagLevelOrder(root)
    print(ans)