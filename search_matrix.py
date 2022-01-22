#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/22 1:47 下午
# @Author  : xinming
# @File    : search_matrix.py
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        t, r = 0, cols-1

        while t<rows and r >=0:
            value =  matrix[t][r]
            if target < value:
                r-=1
            elif target > value:
                t+=1
            else:
                return True
        return False

if __name__=='__main__':
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    out = Solution().searchMatrix(matrix, target)
    print(out)
