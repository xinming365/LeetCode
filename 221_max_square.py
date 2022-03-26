#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/26 11:06 下午
# @Author  : xinming
# @File    : 221_max_square.py
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for i in range(cols)] for i in range(rows)]
        dp[0][0] = 1 if matrix[0][0]==1 else 0
        max_side = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]=="1":
                    if r==0 or c==0:
                        dp[r][c]=1
                    else:
                        dp[r][c]=min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])+1
                max_side = max(max_side, dp[r][c])
        print(max_side)
        return max_side**2

if __name__=='__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"]]
    out = Solution().maximalSquare(matrix=matrix)
    print(out)
