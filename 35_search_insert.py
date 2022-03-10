#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 11:10 上午
# @Author  : xinming
# @File    : 35_search_insert.py

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
            else:
                return mid
        return left

