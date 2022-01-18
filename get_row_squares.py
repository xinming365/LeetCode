#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/18 4:52 下午
# @Author  : xinming
# @File    : get_row_squares.py
from typing import List


def get_next_row(row):
    next_row=[1]
    for i in range(len(row)-1):
        value = row[i]+row[i+1]
        next_row.append(value)
    next_row.append(1)
    return next_row

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        init_row = [1]
        if rowIndex==0:
            return init_row
        for i in range( rowIndex):
            current = get_next_row(init_row)
            init_row = current

        return current

if __name__=='__main__':
    s =3
    out = Solution().getRow(s)
    print(out)