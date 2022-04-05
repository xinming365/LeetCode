#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 8:51 下午
# @Author  : xinming
# @File    : 343_interger_break.py

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        for i in range(2, n+1):
            for j in range(i):
                dp[i]=max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]

if __name__=='__main__':
    n = 10
    out = Solution().integerBreak(n=n)
    print(out)