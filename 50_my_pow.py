#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/20 9:44 下午
# @Author  : xinming
# @File    : 50_my_pow.py

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def get_pow(n):
            if n==0:
                return 1
            y = get_pow(n//2)
            if n%2==0:
                out = y*y
            else:
                out = x * y*y
            return out
        # return  get_pow(n)
        return  get_pow(n) if n>0 else 1/get_pow(-n)

class Solution2:
    def myPow(self, x: float, n: int) -> float:
        def get_pow(N):
            ans = 1
            x_cont = x
            while N:
                if N%2==1:
                    ans = ans*x_cont
                x_cont = x_cont*x_cont
                N = N//2
            return ans
        return  get_pow(n) if n>0 else 1/get_pow(-n)


if __name__=='__main__':
    x_s = 2
    n_s = -2
    out = Solution().myPow(x_s, n_s)
    print(out)