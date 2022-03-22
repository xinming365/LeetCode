#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/20 5:49 下午
# @Author  : xinming
# @File    : 264_ugly_number.py


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[0 for i in range(n)]
        dp[0]=1
        p2, p3, p5=0,0,0

        for i in range(1, n):
            dp[i]=min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
            if dp[i]==dp[p2]*2:
                p2+=1
            if dp[i]==dp[p3]*3:
                p3+=1
            if dp[i]==dp[p5]*5:
                p5+=1
        return dp[n-1]

if __name__=='__main__':
    datas = [1,2,4,10]
    for n in datas:
        out = Solution().nthUglyNumber(n=n)
        print(out)
