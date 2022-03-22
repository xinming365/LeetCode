#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/20 4:18 下午
# @Author  : xinming
# @File    : 91_num_decodings.py

class Solution(object):
    def numDecodings(self, s):

        if not s:
            return None
        if s[0]=='0':
            return 0
        n = len(s)
        dp = [0 for i in range(n)]
        dp[0]=1

        for i in range(1, n):
            if s[i]!='0':
                dp[i]+=dp[i-1]

            if s[i-1]!='0' and (int(s[i-1])*10 + int(s[i]))<=26:
                if i>1:
                    dp[i]+=dp[i-2]
                else:
                    dp[i]+=1

        return dp[n-1]

if __name__=='__main__':
    s = '1226'
    s='06'
    out = Solution().numDecodings(s=s)
    print(out)