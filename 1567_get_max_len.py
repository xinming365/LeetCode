#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 12:01 下午
# @Author  : xinming
# @File    : 1567_get_max_len.py

from typing import List
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        # 存放乘积为正/负的最长子树组的长度
        positive, negative = int(nums[0] > 0), int(nums[0] < 0)
        max_pos = positive
        for i in range(1, n):
            if nums[i]>0:
                positive = positive+1
                negative = (negative+1 if negative>0 else 0)
            elif nums[i]<0:
                np = (negative+1 if negative>0 else 0)
                nn = positive+1
                negative = nn
                positive = np
            else:
                negative=0
                positive=0
            max_pos = max(max_pos, positive)
        return max_pos

class Solution2:
    def getMaxLen(self, nums: List[int]) -> int:
        length = len(nums)
        positive, negative = int(nums[0] > 0), int(nums[0] < 0)
        maxLength = positive

        for i in range(1, length):
            if nums[i] > 0:
                positive += 1
                negative = (negative + 1 if negative > 0 else 0)
            elif nums[i] < 0:
                newPositive = (negative + 1 if negative > 0 else 0)
                newNegative = positive + 1
                positive, negative = newPositive, newNegative
            else:
                positive = negative = 0
            maxLength = max(maxLength, positive)

        return maxLength


if __name__=='__main__':
    datas = [[1,0, 0, 0, 0],  [0,1,-2,-3,-4], [-1,-2,-3,0,1]]
    for data in datas:
        out = Solution2().getMaxLen(nums=data)
        print(out)


