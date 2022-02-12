#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/10 2:50 下午
# @Author  : xinming
# @File    : 108_sorted_array_to_BST.py
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def traverse(left, right):
            if left > right:
                return None

            mid = (left+right)//2
            root = TreeNode(nums[mid])
            root.left = traverse(left, mid-1)
            root.right = traverse(mid+1, right)
            return root
        return traverse(0, len(nums)-1)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


if __name__=='__main__':
    array = [1,2,3,4,5,6,7,8]
    tree_node = Solution().sortedArrayToBST(nums=array)
