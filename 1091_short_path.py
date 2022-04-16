#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/6 10:53 上午
# @Author  : xinming
# @File    : 1091_short_path.py

from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1

        visited = {}
        visited[(0, 0)] = True
        que = deque()
        que.appendleft((0, 0))

        n = len(grid)
        if n == 1:
            return 1
        path = 1
        while que:
            for _ in range(len(que)):
                x, y = que.pop()
                for delta_x, delta_y in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                    nx = x + delta_x
                    ny = y + delta_y
                    # dict.get() 没出现过的返回None。
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and not visited.get((nx, ny)):
                        if nx == n - 1 and ny == n - 1:
                            return path + 1
                        que.appendleft((nx, ny))
                        visited[(nx, ny)] = True
            path += 1
        return -1


if __name__ == '__main__':
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    out = Solution().shortestPathBinaryMatrix(grid=grid)
    print(out)
