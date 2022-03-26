#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/23 12:12 下午
# @Author  : xinming
# @File    : 153_find_min.py
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]<nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[left]

