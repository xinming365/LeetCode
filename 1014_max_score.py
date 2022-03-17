#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 8:22 下午
# @Author  : xinming
# @File    : 1014_max_score.py

from typing import List
class Solution2:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n= len(values)
        max_points = 0
        for i in range(n-1):
            for j in range(i+1, n):
                points = values[i]+values[j]-(j-i)
                max_points = max(points, max_points)
        return max_points

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        max_i = values[0]+0
        max_score = 0
        for j in range(1, n):
            max_score = max(max_score, max_i + values[j]-j)
            max_i = max(max_i, values[j]+j)
        return max_score

if __name__=='__main__':
    values_data = [[1,3,5]]
    for data in values_data:
        out = Solution().maxScoreSightseeingPair(data)
        print(out)