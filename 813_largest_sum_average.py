#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/19 10:47 下午
# @Author  : xinming
# @File    : 813_largest_sum_average.py

from typing import List
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n=len(nums)
        prefix = [0 for i in range(n)]
        prefix[0]=nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1]+nums[i]

        dp = [[0 for i in range(k+1)] for j in range(n)]
        for i in range(n):
            dp[i][0] = prefix[i]/(i+1)

            for kk in range(k):
                if kk <=i:
                    for j in range(i):
                        dp[i][kk]=max(dp[i][kk], dp[j][kk-1]+ (prefix[i]-prefix[j])/(i-j))
                else:
                    break
        return dp[n-1][k-1]

if __name__=='__main__':
    # nums = [9,1,2,3,9]
    nums = [1,2,3,4,5,6,7]
    k = 3

    out = Solution().largestSumOfAverages(nums=nums, k=k)
    print(out)

