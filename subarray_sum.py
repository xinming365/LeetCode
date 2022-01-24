#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/24 8:27 下午
# @Author  : xinming
# @File    : subarray_sum.py
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        pre_dict={0:1} # 第一次就遇见了满足和为k的子序列。
        pre_sum=0
        res=0

        for i in range(length):
            pre_sum+=nums[i]
            sub_sum = pre_sum-k
            if sub_sum in pre_dict:
                res+=pre_dict[sub_sum]
            if pre_sum not in pre_dict.keys():
                pre_dict[pre_sum]=1
            else:
                pre_dict[pre_sum]+=1
        return res

def subarraySum_1(nums: List[int], k: int) -> int:
    res=0
    length=len(nums)
    for i in range(length):
        pre_sum=0
        for j in range(i, length):
            pre_sum+=nums[j]
            if pre_sum==k:
                res+=1
    return res

if __name__=='__main__':
    nums=[1,2, 3]
    target = 3
    out = Solution().subarraySum(nums, target)
    print(out)