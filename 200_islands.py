#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/2 11:12 下午
# @Author  : xinming
# @File    : 200_islands.py
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(grid, r, c):
            grid[r][c]="0"
            for i,j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0<=i<rows and 0<=j<cols and grid[i][j]=="1":
                    dfs(grid, i, j)
        out = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    out+=1
                    dfs(grid, r, c)
        return out

if __name__=='__main__':
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    out = Solution().numIslands(grid=grid)
    print(out)