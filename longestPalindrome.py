#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/24 9:20 下午
# @Author  : xinming
# @File    : longestPalindrome.py

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_str={}
        res=0
        for i in s:
            if i not in dict_str.keys():
                dict_str[i]=1
            else:
                dict_str[i]+=1
        for k, v in dict_str.items():
            if v%2==0:
                res+=v
            else:
                res+=(v-1)
            if v%2==1 and res%2==0:
                res=res+1
        return res

if __name__=='__main__':
    nums='aefbccccdd'
    out = Solution().longestPalindrome(nums)
    print(out)