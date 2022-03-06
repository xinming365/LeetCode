#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 10:46 下午
# @Author  : xinming
# @File    : 26_remove_duplicates.py

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        fast = slow =1
        while  fast<=length-1:
            if nums[fast]!=nums[fast-1]:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        return slow, nums[:slow]






if __name__=='__main__':
    nums = [0,1,1,1,2,2,3,3,4]
    out = Solution().removeDuplicates(nums)
    print(out)
