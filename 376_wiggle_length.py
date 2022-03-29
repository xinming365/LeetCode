#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 2:57 下午
# @Author  : xinming
# @File    : 376_wiggle_length.py

from typing import List
class Solution2:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return n
        wig_len =2 if (nums[1]-nums[0])!=0 else 1
        prev_num = nums[1]-nums[0]
        for i in range(2, n):
            diff = nums[i]-nums[i-1]
            if (diff>0 and prev_num<=0) or (diff<0 and prev_num>=0):
                wig_len+=1
                prev_num = diff
        return wig_len

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return n
        diff=[0 for i in range(n-1)]
        temp = nums[0]
        for i in range(1, n):
            diff[i-1]=nums[i]-temp
            temp =  nums[i]

        dp = [1 for i in range(n-1)]
        for i in range(1, len(diff)):
            for j in range(i):
                if (diff[i]>0 and diff[j]<0) or (diff[i]<0 and diff[j]>0):
                    dp[i]=max(dp[j]+1, dp[i])
        if max(dp)==1 and nums[-1]==nums[-2]:
            return 1
        else:
            return max(dp)+1

if __name__=='__main__':
    # nums = [1,7,4,9,2,5]
    # nums = [1,17,5,10,13,15,10,5,16,8]
    # nums = [0, 0]
    nums = [1,2,3,4,5,6,7,8,9]
    out  = Solution().wiggleMaxLength(nums=nums)
    print(out)
