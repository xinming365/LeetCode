#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 7:27 下午
# @Author  : xinming
# @File    : 542_update_matrix.py

from typing import List
import collections

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[0] * n for _ in range(m)]
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        # 将所有的 0 添加进初始队列中
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)

        # 广度优先搜索
        while q:
            i, j = q.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return dist

if __name__=='__main__':
    # matrix = [[0,0,0],[0,1,0],[0,0,0]]
    matrix = [[0,0,0],[0,1,0],[1,1,1]]
    out = Solution().updateMatrix(matrix=matrix)
    print(out)
