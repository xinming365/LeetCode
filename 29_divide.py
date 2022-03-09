#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 5:40 下午
# @Author  : xinming
# @File    : 29_divide.py

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31-1

        if dividend == INT_MAX and divisor == 1:
            return INT_MAX
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        a = abs(dividend)
        b = abs(divisor)
        res = 0
        # 通过移位运算分解
        # a = b * 2^(i1) + b * 2^(i2) + .... + c   (c < b)
        #    = b * (2 ^ i1 + 2 ^ i2 + ...) + c
        for i in range(31, -1, -1):
            if (b<<i)<=a:
                res = res + (1<<i)
                a = a - (b<<i)
        # if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
        if (dividend>0)==(divisor>0):
            res = -res
        return res



if __name__=='__main__':
    dividend = -50
    divisor = 3
    out = Solution().divide(dividend, divisor)
    print(out)