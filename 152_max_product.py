#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 11:28 上午
# @Author  : xinming
# @File    : 152_max_product.py

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = nums[0]
        curr_max = 1
        curr_min = 1
        for i in range(n):
            unchanged_min = curr_min
            unchanged_max = curr_max
            curr_max = max(unchanged_max*nums[i], max(unchanged_min*nums[i], nums[i]))
            curr_min = min(unchanged_max*nums[i], min(unchanged_min*nums[i], nums[i]))
            max_product = max(max_product, curr_max)
        return max_product

if __name__=='__main__':
    datas = [[-4, -3, -2]]
    for data in datas:
        out = Solution().maxProduct(nums=data)
        print(out)