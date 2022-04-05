#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 8:37 下午
# @Author  : xinming
# @File    : 377_combination_sum.py

from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for i in range(target+1)]
        dp[0]=1
        for i in range(target+1):
            for num in nums:
                if num <=i:
                    dp[i]+=dp[i-num]
        return dp[target]

if __name__=='__main__':
    nums = [1,2,3]
    target = 4
    out = Solution().combinationSum4(nums=nums, target=target)
    print(out)