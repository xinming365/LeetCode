#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/12 2:26 下午
# @Author  : xinming
# @File    : 105_build_tree.py

# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        index = {}
        for i, e in enumerate(inorder):
            index[e]=i

        def build_tree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left>preorder_right:
                return None
            root = preorder[preorder_left]
            root_node = TreeNode(val=root)

            inorder_root = index[root]
            sub_size = inorder_root-1-inorder_left+1
            root_node.left = build_tree(preorder_left+1, preorder_left+sub_size,
                                        inorder_left, inorder_root-1)
            root_node.right = build_tree(preorder_left+sub_size+1, preorder_right,
                                         inorder_root+1, inorder_right)
            return root_node
        n = len(preorder)
        return build_tree(0, n-1, 0, n-1)