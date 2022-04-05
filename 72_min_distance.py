#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 9:58 下午
# @Author  : xinming
# @File    : 72_min_distance.py

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        if n * m == 0:
            return n + m

        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(n+1):
            dp[i][0]=i

        for j in range(m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                low_left = dp[i-1][j-1]
                if word1[i-1]!=word2[j-1]:
                    low_left = low_left+1
                dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, low_left)
        return dp[n][m]

if __name__=='__main__':
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 13

    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 3

    word1 = "horse"
    word2 = "ros"
    out = Solution().minDistance(word1, word2)
    print(out)