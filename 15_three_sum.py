#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/25 10:46 下午
# @Author  : xinming
# @File    : 15_three_sum.py

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []
        for i in range(n-2):
            second = n - 1
            if i>0 and nums[i] == nums[i - 1]:
                continue
            residual = -nums[i]
            for first in range(i+1, n):
                if first > i+1 and nums[first]==nums[first-1]:
                    continue
                while first < second and nums[first]+nums[second]>residual:
                    second-=1
                if first==second:
                    break
                if nums[first]+nums[second]==residual:
                    res.append([nums[i], nums[first], nums[second]])
        return res

if __name__=='__main__':
    nums = [-1,0,1,2,-1,-4]
    nums = [0,0,0,0]
    out = Solution().threeSum(nums = nums)
    print(out)