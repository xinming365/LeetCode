#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/26 10:08 下午
# @Author  : xinming
# @File    : 62_unique_path.py

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n] + [[1]+[0]*(n-1) for i in range(m-1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]