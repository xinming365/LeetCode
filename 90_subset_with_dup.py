#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 3:10 下午
# @Author  : xinming
# @File    : 90_subset_with_dup.py

class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        n = len(nums)
        nums.sort()

        def back_track(idx, tmp):
            if tmp not in res:
                res.append(tmp[:])
            for i in range(idx, n):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                back_track(i+1, tmp+[nums[i]])

        back_track(0, [])
        return res

class Solution2(object):
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, res, path + [nums[i]])


if __name__=='__main__':
    nums = [1,2,2]
    out = Solution2().subsetsWithDup(nums=nums)
    print(out)