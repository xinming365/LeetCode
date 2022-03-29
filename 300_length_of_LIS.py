#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 2:15 下午
# @Author  : xinming
# @File    : 300_length_of_LIS.py

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        print(dp)
        return max(dp)

if __name__=='__main__':
    # nums = [10,9,2,5,3,7,101,18]
    nums = [1,3,6,7,9,4,10,7,6]
    out = Solution().lengthOfLIS(nums=nums)
    print(out)
