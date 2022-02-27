#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/27 11:25 下午
# @Author  : xinming
# @File    : 20_is_valid.py

class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        my_dict = {']':'[', ')':'(', '}':'{'}
        for c in s:
            if my_stack and c in my_dict.keys():
                if my_stack[-1]==my_dict[c]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(c)
        return not my_stack

if __name__=='__main__':
    out = Solution().isValid(s=')')
    print(out)