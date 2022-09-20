#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/20 3:58 下午
# @Author  : xinming
# @File    : 95_different_binary_search_tree.py

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_tree(start, end):

            if start > end:
                return [None]

            all_tree = []
            for i in range(start, end+1):
                left_tree = generate_tree(start, i-1)
                right_tree = generate_tree(i+1, end)
                for l in left_tree:
                    for r in right_tree:
                        base = TreeNode(i)
                        base.left = l
                        base.right = r
                        all_tree.append(base)
            return all_tree
        return  generate_tree(1, n) if n >0 else []

if __name__=='__main__':
    out = Solution().generateTrees(5)
    print(out)