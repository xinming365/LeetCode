#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 11:33 上午
# @Author  : xinming
# @File    : 167_two_sum.py

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left <=right:
            if numbers[left]+numbers[right]>target:
                right-=1
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                return [left+1, right+1]
        return [-1, -1]

if __name__=='__main__':
    nums = [2,7,11,15]
    target = 9
    out = Solution().twoSum(numbers=nums, target=9)
    print(out)
