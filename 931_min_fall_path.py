#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/22 10:56 上午
# @Author  : xinming
# @File    : 931_min_fall_path.py
from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        depth = len(matrix)
        width = len(matrix[0])

        dp = [ [0 for i in range(width)] for i in range(depth)]

        for i in range(width):
            dp[0][i] = matrix[0][i]

        for row in range(1, depth):
            for col in range(width):
                if col==0 :
                    dp[row][col]= min(dp[row-1][col], dp[row-1][col+1]) + matrix[row][col]
                elif col==width-1:
                    dp[row][col]= min(dp[row-1][col], dp[row-1][col-1]) + matrix[row][col]
                else:
                    min_path = min(dp[row-1][col], dp[row-1][col-1], dp[row-1][col+1])
                    dp[row][col]= min_path + matrix[row][col]
        return min(dp[depth-1])


if __name__=='__main__':
    matrix = [[-19,57],[-40,-5]]
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    out = Solution().minFallingPathSum(matrix=matrix)
    print(out)