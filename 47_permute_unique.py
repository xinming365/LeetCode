#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 3:48 下午
# @Author  : xinming
# @File    : 47_permute_unique.py
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return None
            else:
                for i in range(n):
                    if i>0 and nums[i]==nums[i-1]:
                        continue
                    backtrack(nums[:i]+nums[i+1:], tmp+[nums[i]])
        backtrack(nums, [])
        return res


if __name__=='__main__':
    nums = [1,1,2]
    out = Solution().permuteUnique(nums=nums)
    print(out)

