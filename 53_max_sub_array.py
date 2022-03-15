#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 11:35 上午
# @Author  : xinming
# @File    : 53_max_sub_array.py

from typing import List
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        max_ans = nums[0]
        n = len(nums)
        for i in range(n):
            pre = max(pre+nums[i], nums[i])
            max_ans = max(max_ans, pre)
        return max_ans

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ans = float('-inf')
        n = len(nums)
        sum = 0
        for i in range(n):
            sum += nums[i]
            max_ans = max(max_ans, sum)

            if sum<0:
                sum=0
        return max_ans



if __name__=='__main__':
    nums_data = [[-2,1,-3,4,-1,2,1,-5,4], [1], [2,3,-4,2,4]]
    for nums in nums_data:
        max_ans = Solution().maxSubArray(nums = nums)
        print(max_ans)


