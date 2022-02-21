#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 10:45 下午
# @Author  : xinming
# @File    : 11_max_area.py

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = 0
        while l<r:
            d = r-l
            area = min(height[l], height[r])*d
            max_area = max(max_area, area)
            if height[l] <  height[r]:
                l+=1
            else:
                r-=1
        return max_area


if __name__=='__main__':
    height = [1,8,6,2,5,4,8,3,7]
    out = Solution().maxArea(height)
    print(out)