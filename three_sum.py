#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/14 9:18 下午
# @Author  : xinming
# @File    : three_sum.py

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        out = []
        for first in range(length):
            if first > 0 and nums[first]==nums[first-1]:
                continue
            third=length-1
            target = -nums[first]
            for second in range(first+1, length):
                if second > first+1 and nums[second]==nums[second-1]:
                    continue

                while second < third and nums[second]+nums[third]>target:
                    third-=1
                if third==second:
                    break
                if nums[second]+nums[third]==target :
                    out.append([nums[first], nums[second], nums[third]])


        return out

if __name__=='__main__':
    # nums=[-1,0,1,2,-1,-4]
    nums=[0,0,0]
    nums=[-1,0,1,2,-1,-4]
    target = 6
    out = Solution().threeSum(nums)
    print(out)