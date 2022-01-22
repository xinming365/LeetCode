#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/18 5:15 下午
# @Author  : xinming
# @File    : rotate_matrix.py
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            if n%2==0:
                in_n = n-2*i
            else:
                in_n = n - 2*i
            for x in range(in_n-1):
                j=i+x
                ci = j
                cj = n-i-1
                matrix[i][j],  matrix[ci][cj] = matrix[ci][cj], matrix[i][j]

                matrix[i][j], matrix[cj][n-ci-1] = matrix[cj][n-ci-1], matrix[i][j]

                matrix[i][j], matrix[n-ci-1][n-cj-1] = matrix[n-ci-1][n-cj-1], matrix[i][j]


if __name__=='__main__':

    nums=[[1,2,3],[4,5,6],[7,8,9]]
    # nums = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Solution().rotate(nums)

    print(nums)

