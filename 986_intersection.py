#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/26 11:55 下午
# @Author  : xinming
# @File    : 986_intersection.py

from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1 = len(firstList)
        n2 = len(secondList)

        i, j = 0, 0
        res = []
        while i<n1 and j<n2:
            low = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])

            if low <= high:
               res.append([low, high])

            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
        return res

if __name__=='__main__':
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]

    out = Solution().intervalIntersection(firstList=firstList, secondList=secondList)
    print(out)


