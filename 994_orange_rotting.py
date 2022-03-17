#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 8:55 下午
# @Author  : xinming
# @File    : 994_orange_rotting.py

from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        height = len(grid)

        time = 0
        rotted = [(i, j, time) for i in range(height) for j in range(width) if grid[i][j]==2]
        rotted = deque(rotted)

        while rotted:
            i,j, time = rotted.popleft()
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0<=ni<height and 0<=nj<width and grid[ni][nj]==1:
                    grid[ni][nj]=2
                    rotted.append((ni, nj, time+1))

        for row in grid:
            if 1 in row:
                return -1
        return time


if __name__=='__main__':
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    out = Solution().orangesRotting(grid)
    print(out)