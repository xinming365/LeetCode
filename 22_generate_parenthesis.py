#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/3 11:00 上午
# @Author  : xinming
# @File    : 22_generate_parenthesis.py
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def back_track(temp_s, left, right):
            if (left+right)>=2*n:
                ans.append(''.join(temp_s))
                return None

            if left < n:
                temp_s.append('(')
                back_track(temp_s, left+1, right)
                temp_s.pop()
            if right < left:
                temp_s.append(')')
                back_track(temp_s, left, right+1)
                temp_s.pop()

        back_track([], 0, 0)
        return ans



if __name__=='__main__':
    ans  = Solution().generateParenthesis(3)
    print(ans)