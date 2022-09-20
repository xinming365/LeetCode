#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 12:01 上午
# @Author  : xinming
# @File    : 57_insert.py

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        merged = []
        placed  = False
        for i in intervals:
            if i[-1] < newInterval[0]:

                merged.append(i)
            elif i[0]>newInterval[1]:

                if not placed:
                    merged.append([left, right])
                    placed = True

                merged.append(i)
            else:
                left = min(i[0], left)
                right = max(i[1], right)

        if not placed:
            merged.append([left, right])
        return merged

if __name__=='__main__':
    # intervals = [[1,3],[6,9]]
    # newInterval = [2,5]
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    out = Solution().insert(intervals=intervals, newInterval=newInterval)
    print(out)

