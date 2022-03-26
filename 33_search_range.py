#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/22 11:09 下午
# @Author  : xinming
# @File    : 33_search_range.py

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left<=right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            if nums[0]<= nums[mid]:
                if nums[0]<= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid+1
            else:
                if nums[mid]< target <=nums[n-1]:
                    left = mid+1
                else:
                    right = mid - 1
        return -1

if __name__=='__main__':
    # nums = [4,5,6,7,0,1,2]
    # target = 0

    nums = [4,5,6,7,0,1,2]
    target = 3
    out = Solution().search(nums, target)
    print(out)

