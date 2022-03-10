#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 11:36 上午
# @Author  : xinming
# @File    : 977_sorted_squares.py

from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        left = 0
        right = n-1
        res=[]
        while left<=right:
            if nums[left]**2 < nums[right]**2:
                val = nums[right]**2
                right -=1
            else:
                val = nums[left]**2
                left +=1
            res.insert(0, val)
        return res

if __name__=='__main__':
    nums = [-4,-1,0,3,10]
    out = Solution().sortedSquares(nums)
    print(out)
