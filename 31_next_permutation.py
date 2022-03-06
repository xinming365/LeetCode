#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 10:12 下午
# @Author  : xinming
# @File    : 31_next_permutation.py
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i>0 and nums[i] >= nums[i+1]:
            i-=1

        # find the larger value at the right of nums[i]
        j=len(nums)-1
        while j>0 and nums[i] >= nums[j]:
            j-=1
        nums[i], nums[j] = nums[j], nums[i]

        if i!=j:
            left = i+1
        else:
            left=0
        right = len(nums)-1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1



if __name__=='__main__':
    nums = [1, 5, 1]
    Solution().nextPermutation(nums)
    print(nums)