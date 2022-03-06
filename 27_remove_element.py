#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 11:15 下午
# @Author  : xinming
# @File    : 27_remove_element.py

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left=0
        for i in range(n):
            if nums[i]!=val:
                nums[left]=nums[i]
                left+=1
        return left

if __name__=='__main__':
    nums = [3, 2, 2, 3]
    val = 3
    out = Solution().removeElement(nums, val)
    print(out)