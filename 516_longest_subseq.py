#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 1:35 下午
# @Author  : xinming
# @File    : 516_longest_subseq.py
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # 使用二维的dp存储(i,j)
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i]=1
            for j in range(i+1, n):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]

if __name__=='__main__':
    s = "bbbab"
    out = Solution().longestPalindromeSubseq(s=s)
    print(out)