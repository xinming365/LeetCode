#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/22 6:49 下午
# @Author  : xinming
# @File    : 34_search_range.py
from typing import List, Tuple, Union

class Solution:
    def searchRange(self, nums: List[int], target: int) -> Tuple[Union[int, List[int]], Union[int, List[int]]]:

        if not nums:
            return [-1, -1]
        def find_border(nums, target, right_border):
            index = -1
            left= 0
            right = len(nums)-1
            while left<=right:
                mid = (left+right)//2
                if target < nums[mid]:
                    right = mid-1
                elif nums[mid]<target:
                    left = mid+1
                else:
                    index = mid # 覆盖这个边界。
                    if right_border:
                        left = mid+1
                    else:
                        right = mid - 1
            return index
        first = find_border(nums, target, right_border=False)
        last = find_border(nums, target, right_border=True)
        return [first, last]
if __name__=='__main__':
    nums = [5,7,7,8,8,10]
    target = 8
    out = Solution().searchRange(nums, target)
    print(out)

