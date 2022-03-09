#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 7:39 下午
# @Author  : xinming
# @File    : 704_binary_search.py
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if target < nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid+1
            else:
                return  mid
        return -1


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, left, right):

            if left>right:
                return -1
            mid = (left+right)//2
            mid_val = nums[mid]

            if target == mid_val:
                return mid
            elif target> mid_val:
                # ⚠️：回溯到最后一层的时候没有return，返回None
                return binary_search(nums, mid+1, right)
            else:
                return binary_search(nums, left, mid-1)

        n=len(nums)
        out = binary_search(nums, 0, n-1)
        return out



if __name__=='__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    out = Solution().search(nums, 9)
    print(out)