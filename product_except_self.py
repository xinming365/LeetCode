#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/24 11:18 上午
# @Author  : xinming
# @File    : product_except_self.py
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lens=len(nums)
        prefix, suffix=1,1
        answer=[1 for i in range(lens)]
        for i in range(lens):
            answer[i]*=prefix
            answer[lens-i-1]*=suffix
            prefix*=nums[i]
            suffix*=nums[lens-i-1]
        return answer

if __name__=='__main__':
    nums=[1,2,3,4]
    out = Solution().productExceptSelf(nums)
    print(out)