#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/26 9:39 下午
# @Author  : xinming
# @File    : 304_num_matrix.py

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.mat = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.pre = [[0 for i in range(self.cols+1)] for i in range(self.rows+1)]
        for r in range(1, self.rows+1):
            for c in range(1, self.cols+1):
                self.pre[r][c] = self.pre[r-1][c]+self.pre[r][c-1]-self.pre[r-1][c-1]+self.mat[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        _pre=self.pre
        out =_pre[row2+1][col2+1]-_pre[row2+1][col1]-_pre[row1][col2+1]+_pre[row1][col1]
        return out


