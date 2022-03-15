#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/11 11:00 下午
# @Author  : xinming
# @File    : 557_reverse_words.py

class Solution(object):
    def reverseWords(self, s):

        return " ".join(word[::-1] for word in s.split(" "))

if __name__=='__main__':
    s = "Let's take LeetCode contest"
    out = Solution().reverseWords(s)
    print(out)