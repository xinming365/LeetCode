#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/21 11:57 下午
# @Author  : xinming
# @File    : 17_letter_combinations.py

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        def back_track(combinations, digits):
            if len(digits)==0:
                res.append(combinations)
            else:
                for c in phoneMap[digits[0]]:
                    back_track(combinations+c, digits[1:])
            return res
        out = back_track('', digits)
        return out




if __name__=='__main__':
    combinations = Solution().letterCombinations(digits='23')
    print(combinations)