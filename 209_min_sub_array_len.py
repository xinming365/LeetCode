#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 11:50 下午
# @Author  : xinming
# @File    : 209_min_sub_array_len.py

from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0

        n = len(nums)
        res = n+1
        sum = 0
        while end < n:
            sum += nums[end]
            while sum>=target:
                res = min(res, end-start+1)
                sum-=nums[start]
                start+=1
            end+=1
        return 0 if res==n+1 else res

if __name__=='__main__':
    target = 7
    nums = [2,3,1,2,4,3]
    out = Solution().minSubArrayLen(target=target, nums=nums)
    print(out)
