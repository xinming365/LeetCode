#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/18 10:34 下午
# @Author  : xinming
# @File    : 139_word_break.py
from typing import List
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(n):
            for j in range(i+1,n+1):
                if(dp[i] and (s[i:j] in wordDict)):
                    dp[j]=True
        return dp[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp = [False for i in range(n+1)]
        dp[0]=True
        for i in range(1, n+1):
            for j in range(0, i):
                if (dp[j] and (s[j:i] in wordDict)):
                    dp[i]=True
                    break
        return dp[-1]

if __name__=='__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    out = Solution().wordBreak(s, wordDict)
    print(out)


