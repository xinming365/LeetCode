#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/22 3:03 下午
# @Author  : xinming
# @File    : erase_overlap_intervals.py
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        nums=1
        length = len(intervals)
        breakpoint=intervals[0][1]
        for i in range(1, length):
            if intervals[i][0]>= breakpoint:
                nums+=1
                breakpoint=intervals[i][1]
        return length-nums

class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        if N == 0: return 0

        intervals.sort(key=lambda x: x[1]) #按右边界排序
        breakpoint = intervals[0][1] #最左元素的右边界作为基准
        cnt = 1

        #记录非交叉区间的个数 局部最优：从左向右(优先考量右边界小的区间)
        for i in range(1,N):
            if intervals[i][0] >= breakpoint: #不交叉
                cnt += 1
                breakpoint = intervals[i][1]

        return N - cnt



if __name__=='__main__':
    # s = [ [1,2], [2,3], [3,4], [1,3] ]
    s = [[1,2],[1,2],[1,2]]
    out = Solution().eraseOverlapIntervals(s)
    print(out)

