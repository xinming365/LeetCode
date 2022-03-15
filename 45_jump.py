#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 11:18 上午
# @Author  : xinming
# @File    : 45_jump.py

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        reach=0
        n = len(nums)
        step = 0
        stop = 0
        for i in range(n-1):
            # 维护最远跳跃距离
            reach = max(reach, i+nums[i])
            # 跳跃右边界，也是下一个起跳位置。一开始可以不是最远，但是在到达时，会更新到最远。
            if i==stop:
                stop = reach
                step+=1
        return step

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         maxPos, end, step = 0, 0, 0
#         for i in range(n - 1):
#             if maxPos >= i:
#                 maxPos = max(maxPos, i + nums[i])
#                 if i == end:
#                     end = maxPos
#                     step += 1
#         return step


if __name__=='__main__':
    nums = [2,3,1,1,4]
    step = Solution().jump(nums = nums)
    print(step)