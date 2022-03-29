#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/28 11:52 下午
# @Author  : xinming
# @File    : 438_find_anagrams.py
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        s_window = [0 for i in range(26)]
        p_window = [0 for i in range(26)]


        for i in range(p_len):
            p_window[ord(p[i])-ord('a')]+=1
            s_window[ord(s[i])-ord('a')]+=1

        if s_window==p_window:
            ans.append(0)

        for i in range(s_len-p_len):
            s_window[ord(s[i])-ord('a')]-=1
            s_window[ord(s[i+p_len])-ord('a')]+=1

            if s_window==p_window:
                ans.append(i+1)
        return ans


if __name__=='__main__':
    s = "cbaebabacd"
    p = "abc"
    out = Solution().findAnagrams(s=s, p=p)
    print(out)