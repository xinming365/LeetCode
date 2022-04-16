#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 1:31 下午
# @Author  : xinming
# @File    : 78_subsets.py

from typing import List
class Solution:
    def subsets(self, nums):
        if not nums:
            return None

        res = []
        n = len(nums)

        def back_track(idx, sub_num):
            res.append(sub_num)
            for i in range(idx, n):
                back_track(i+1, sub_num+[nums[i]])
        back_track(0, [])
        return res

if __name__=='__main__':
    nums = [1,2,3]
    out = Solution().subsets(nums=nums)
    print(out)