#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 10:36 上午
# @Author  : xinming
# @File    : 918_max_sub_sum.py

from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        pre_max = 0
        pre_min = 0
        max_sum, min_sum = nums[0], nums[0]
        for i in range(n):
            sum+=nums[i]
            pre_max = max(pre_max+nums[i], nums[i])
            max_sum = max(max_sum, pre_max)
            pre_min = min(pre_min+nums[i], nums[i])
            min_sum = min(min_sum, pre_min)
        if max_sum<0:
            return max_sum
        return max(sum-min_sum, max_sum)

if __name__=='__main__':
    datas = [[1,-2,3,-2], [5,-3,5], [3,-2,2,-3]]
    for data in datas:
        out = Solution().maxSubarraySumCircular(data)
        print(out)