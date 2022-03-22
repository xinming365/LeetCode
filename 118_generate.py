#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/21 11:26 上午
# @Author  : xinming
# @File    : 118_generate.py
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[0 for j in range(i+1)] for i in range(numRows)]
        res[0][0]=1

        for depth in range(1, numRows):
            res[depth][0] = res[depth-1][0]
            for i in range(1, depth):
                res[depth][i] = res[depth-1][i]+res[depth-1][i-1]
            res[depth][depth] = res[depth-1][depth-1]
        return res

if __name__=='__main__':
    out =Solution().generate(5)
    print(out)