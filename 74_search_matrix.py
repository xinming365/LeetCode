#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/23 11:11 上午
# @Author  : xinming
# @File    : 74_search_matrix.py
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        depth = len(matrix)
        width = len(matrix[0])

        left = 0
        right = depth-1
        index_row = 0
        while left<=right:
            mid = (left+right)//2
            if target==matrix[mid][0]:
                return True
            if target< matrix[mid][0]:
                right = mid - 1
            else:
                index_row = mid
                left = mid + 1


        left = 0
        right = width -1
        while left<=right:
            mid = (left+right)//2
            if target == matrix[index_row][mid]:
                return True
            if target < matrix[index_row][mid]:
                right = mid-1
            else:
                left = mid+1
        return False

if __name__=='__main__':
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 13

    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 3

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 11
    out = Solution().searchMatrix(matrix, target)
    print(out)



