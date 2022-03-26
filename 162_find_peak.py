#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/24 12:20 上午
# @Author  : xinming
# @File    : 162_find_peak.py

from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        n = len(nums)
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1

        while left <=right:
            mid = (left+right)//2

            if nums[mid]<nums[mid+1]:
                left = mid+1
            elif nums[mid]>nums[mid+1]:
                right = mid-1
                if nums[mid]>nums[mid-1]:
                    return mid
        return -1

if __name__=='__main__':
    nums = [1,2]
    out = Solution().findPeakElement(nums)
    print(out)
