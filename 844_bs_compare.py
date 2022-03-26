#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/26 11:44 下午
# @Author  : xinming
# @File    : 844_bs_compare.py

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_out(s):
            stack = []
            for i in s:
                if i=='#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return ''.join(stack)
        ss = get_out(s)
        tt = get_out(t)
        if ss==tt:
            return True
        else:
            return False

if __name__=='__main__':
    s = "a##c"
    t = "#a#c"
    out = Solution().backspaceCompare(s,t)
    print(out)