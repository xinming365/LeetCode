#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/27 8:58 下午
# @Author  : xinming
# @File    : 5_longest_palindrome.py

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l < 2:
            return s
        dp = [[False]*l for i in range(l)]
        for i in range(l):
            dp[i][i]=True
        max_len=1
        out_i=0
        for j in range(1, l): # 先填充左下！否则由于被赋予初始化值而出错。
            for i in range(0, j):
                if s[i]!=s[j]:
                    dp[i][j]=False
                else:
                    if j-i<3:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1] # 根据左下确定。
                if dp[i][j]==True and j-i+1>max_len:
                    max_len=j-i+1
                    out_i=i
        return s[out_i:out_i+max_len]

if __name__=='__main__':
    s="aaaa"
    out = Solution().longestPalindrome(s)
    print(out)