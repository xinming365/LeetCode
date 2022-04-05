#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 9:03 下午
# @Author  : xinming
# @File    : 279_num_squares.py

class Solution:
    def numSquares(self, n: int) -> int:
        pass
        # dp = [float('inf') for i in range(n+1)]
        # dp[0]=0
        # dp[1]=1
        # for i in range(2, n+1):
        #     curr = i*i
        #     while j**2<=i:
        #         dp[i]=min(dp[i], dp[i-j**2])
        #     dp[i]=min(dp[i], dp[i-j**2]+1)
        # return dp[n]

from math import sqrt, inf

class Solution2:
    def numSquares(self, n: int) -> int:
        dp = [0] + [inf] * n
        rg = int(sqrt(n))
        for i in range(1, rg + 1):
            curr = i * i
            for j in range(curr,n+1):
                dp[j] = min(dp[j],dp[j-curr]+1)
        return dp[n]


if __name__=='__main__':
    n = 13
    out = Solution().numSquares(n=n)
    print(out)