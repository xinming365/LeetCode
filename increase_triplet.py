#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/23 9:47 下午
# @Author  : xinming
# @File    : increase_triplet.py

from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        first, second = nums[0], max(nums)
        for i in nums:
            if i > second:
                return True
            if i > first:
                second=i
            else:
                first = i
        return False


if __name__=='__main__':
    s = [1,2,3,4,5]
    out = Solution().increasingTriplet(s)
    print(out)