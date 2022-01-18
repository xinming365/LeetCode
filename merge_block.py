#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/16 10:49 下午
# @Author  : xinming
# @File    : merge_block.py
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1]=max(merged[-1][1], i[1])
        return merged




def merge1( intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    left0, right0 = intervals[0]
    ptr=1
    while ptr<len(intervals):
        left, right = intervals[ptr]
        if left<=right0:
            if right > right0:
                right0=right
            intervals[ptr-1][1]=right0
            del intervals[ptr]
        else:
            right0=intervals[ptr][-1]
            ptr+=1

    return intervals

if __name__=='__main__':

    nums=[[1,4],[2,3]]
    out = Solution().merge(nums)

    print(out)