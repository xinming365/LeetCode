#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/26 10:48 下午
# @Author  : xinming
# @File    : 64_min_path_sum.py

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0 for i in range(cols)] for i in range(rows)]

        dp[0][0]=grid[0][0]
        for i in range(1, cols):
            dp[0][i]=dp[0][i-1]+grid[0][i]
        for i in range(1, rows):
            dp[i][0]=dp[i-1][0]+grid[i][0]

        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = min(dp[r-1][c], dp[r][c-1])+grid[r][c]
        return dp[rows-1][cols-1]

if __name__=='__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    out = Solution().minPathSum(grid=grid)
    print(out)

