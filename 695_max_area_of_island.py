#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 10:55 下午
# @Author  : xinming
# @File    : 695_max_area_of_island.py
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        height = len(grid)
        width = len(grid[0])

        max_area = 0

        def dfs(x, y):
            if grid[x][y]==1:
                area.append(1)
            else:
                return [0]
            grid[x][y] = 0
            for mx, my in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0<=mx<height and 0<=my<width and grid[mx][my]==1:
                    dfs(mx, my)

        for x in range(height):
            for y in range(width):
                area=[]
                dfs(x, y)
                area_value = sum(area)
                max_area = max(area_value, max_area)
        return max_area

if __name__=='__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    out = Solution().maxAreaOfIsland(grid=grid)
    print(out)
