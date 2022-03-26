#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/26 10:13 下午
# @Author  : xinming
# @File    : 63_unique_path_with_obstacles.py

from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0 for i in range(cols)] for i in range(rows)]
        dp[0][0]=0 if obstacleGrid[0][0]==1 else 1
        for i in range(1, cols):
            if obstacleGrid[0][i]==1 or dp[0][i-1]==0:
                dp[0][i]=0
            else:
                dp[0][i]=1

        for i in range(1, rows):
            if obstacleGrid[i][0]==1 or dp[i-1][0]==0:
                dp[i][0]=0
            else:
                dp[i][0]=1

        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c]==1:
                    dp[r][c]=0
                else:
                    dp[r][c]=dp[r-1][c]+dp[r][c-1]
        return dp[rows-1][cols-1]

if __name__=='__main__':
    obstacleGrid = [[1,1]]
    out = Solution().uniquePathsWithObstacles(obstacleGrid=obstacleGrid )
    print(out)
