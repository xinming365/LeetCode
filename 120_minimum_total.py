#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/20 8:45 下午
# @Author  : xinming
# @File    : 120_minimum_total.py
import math
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]])->int:
        depth = len(triangle)
        min_path = [[0 for i in range(j+1)] for j in range(depth)]
        min_path[0][0]=triangle[0][0]
        for i in range(1, depth):
            # i最大值为depth-1
            min_path[i][0]=min_path[i-1][0]+triangle[i][0]
            # 有depth个元素，最后一个应该取depth-1。但是这里最大取i-1，即depth-2。
            for j in range(1, i):
                min_path[i][j] = min(min_path[i-1][j], min_path[i-1][j-1])+triangle[i][j]
            min_path[i][i] = min_path[i-1][i-1]+triangle[i][i]

        return min(min_path[depth-1])



if __name__=='__main__':
    # triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    # triangle = [[-10]]
    triangle = [[-1],[2,3],[1,-1,-3]]
    out = Solution().minimumTotal(triangle)
    print(out)