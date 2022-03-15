#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 9:11 上午
# @Author  : xinming
# @File    : 42_trap.py
from typing import List
class Solution1:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        for i in range(n):
            left_max =0
            right_max = 0
            for j in range(i, 0, -1):
                left_max = max(left_max, height[j])
            for j in range(i, n):
                right_max = max(right_max, height[j])
            h = min(left_max, right_max)
            ans+= (h - height[i])
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left_max = [0 for i in range(n)]
        right_max = [0 for i in range(n)]

        # dp初始边界
        left_max[0]=height[0]
        right_max[n-1] = height[n-1]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])
        for i in range(n-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])

        for i in range(n):
            ans += min(left_max[i], right_max[i])-height[i]
        return ans

if __name__=='__main__':
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [4,2,0,3,2,5]
    ans = Solution().trap(height)
    print(ans)
