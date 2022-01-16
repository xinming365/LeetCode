#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/14 10:12 下午
# @Author  : xinming
# @File    : sort_color.py

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        ptr=0
        for i in range(length):
            if nums[i] ==0:
                nums[ptr], nums[i]=nums[i], nums[ptr]
                ptr+=1

        for i in range(ptr, length):
            if nums[i]==1:
                nums[ptr], nums[i]=nums[i], nums[ptr]
                ptr+=1



def bubble_sort(nums):
    length = len(nums)
    for j in range(length):
        for i in range(length-j-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

if __name__=='__main__':

    nums=[2,0,2,1,1,0]
    out = Solution().sortColors(nums)

    print(nums)

