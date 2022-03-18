#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/18 12:57 下午
# @Author  : xinming
# @File    : 46_permute.py

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        k = len(nums)
        path = []
        def back_track(start_index):
            if len(path)==k:
                res.append(path[:])
                return None

            for i in range(start_index, k):
                if nums[i] in path:
                    continue
                path.append(nums[i])

                back_track(start_index)
                path.pop()
        back_track(0)
        return res

if __name__=='__main__':
    out = Solution().permute(nums = [1,2,3])
    print(out)
