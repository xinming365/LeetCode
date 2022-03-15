#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 1:05 下午
# @Author  : xinming
# @File    : 55_can_jump.py

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = 0
        for i in range(n):
            if i <=reach:
                reach=max(reach, i+nums[i])
        if reach>=n-1:
            return True
        else:
            return False

