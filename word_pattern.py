#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/24 10:08 下午
# @Author  : xinming
# @File    : word_pattern.py

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p2ch=dict()
        ch2p=dict()
        str_list = s.split(sep=' ')
        if len(pattern)!=len(str_list):
            return False

        for p, s in zip(pattern, str_list):
            if p not in p2ch.keys():
                p2ch[p]=s
            if s not in ch2p.keys():
                ch2p[s]=p
            if (p2ch[p]!=s) or (ch2p[s]!=p):
                return False
        return True
if __name__=='__main__':
    # pattern = "abba"
    # str = "dog cat cat dog"
    pattern = "abba"
    str = "dog dog dog dog"
    out = Solution().wordPattern(pattern, str)
    print(out)