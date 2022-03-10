#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 11:45 上午
# @Author  : xinming
# @File    : 189_rotate.py

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        def reverse(nums, left, right):
            while left<=right:
                nums[left], nums[right]=nums[right], nums[left]
                left+=1
                right-=1
            # return nums

        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
        # return nums
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[n-k:]+nums[:n-k]

if __name__=='__main__':
    nums=[i for i  in range(1,8)]
    Solution2().rotate(nums, 3)
    print(nums)


