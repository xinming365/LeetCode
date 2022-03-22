#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/20 12:36 上午
# @Author  : xinming
# @File    : 413_number_of_slices.py


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        n  = len(A)
        dp = [0 for i in range(n)]
        for i in range(1, n-1):
            if A[i+1]-A[i]==A[i]-A[i-1]:
                dp[i]=dp[i-1]+1

        return sum(dp)

if __name__=='__main__':
    A = [1,2,3,4,5]
    out = Solution().numberOfArithmeticSlices(A=A)
    print(out)