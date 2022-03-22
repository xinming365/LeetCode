#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/20 10:31 下午
# @Author  : xinming
# @File    : 6_convert.py
from itertools import chain
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s
        x = 0
        res = [[] for i in range(numRows)]
        period = 2*numRows-2
        for i in range(n):
            print(s[i])
            res[x].append(s[i])
            print(res[x])
            x += 1 if x % period < 2 else -1
            print('x:',x)
            #if x % period < numRows-1:
            #    x+=1
            #else:
            #    x-=1
        return ''.join(chain(*res))
class Solution3:
    def convert(self, s: str, numRows: int) -> str:
        r = numRows
        if r == 1 or r >= len(s):
            return s
        mat = [[] for _ in range(r)]
        t, x = r * 2 - 2, 0
        for i, ch in enumerate(s):
            print(ch)
            mat[x].append(ch)
            print(mat[x])
            x += 1 if i % t < 2 else -1
            print('x:',x)
        return ''.join(chain(*mat))


if __name__=='__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    out= Solution().convert(s=s, numRows=numRows)
    print('================================')
    out1= Solution3().convert(s=s, numRows=numRows)
    print(out,out1)



