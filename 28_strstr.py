#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 12:04 上午
# @Author  : xinming
# @File    : 28_strstr.py

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if n==0:
            return 0
        if m<n:
            return -1
        for i in range(m-n+1):
            sub_pattern=haystack[i:i + n]
            if  sub_pattern== needle[:]: #如果在窗口长度字符串是相同的
                return i #返回第i个字符串的位置
        return -1

if __name__=='__main__':
    haystack ="hello"
    needle = "ll"
    # haystack ="abc"
    # needle = "c"

    out = Solution().strStr(haystack, needle)
    print(out)