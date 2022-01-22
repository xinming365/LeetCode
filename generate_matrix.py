#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/22 11:28 上午
# @Author  : xinming
# @File    : generate_matrix.py
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r, t, b=0, n-1, 0, n-1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        size=n*n
        nums = 1
        while nums <= size:
            for i in range(l, r+1):
                mat[t][i]=nums
                nums+=1
            t+=1
            for i in range(t, b+1):
                mat[i][r]=nums
                nums+=1
            r-=1
            for i in range(r, l-1, -1):
                mat[b][i]=nums
                nums+=1
            b-=1
            for i in range(b, t-1, -1):
                mat[i][l]=nums
                nums+=1
            l+=1
        return mat

if __name__=='__main__':
    s =3
    out = Solution().generateMatrix(s)
    print(out)



