#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 11:21 上午
# @Author  : xinming
# @File    : 283_move_zeros.py
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        j=0
        for i in range(n):
            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j +=1
if __name__=='__main__':
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums=nums)
    print(nums)
