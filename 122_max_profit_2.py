#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 8:41 下午
# @Author  : xinming
# @File    : 122_max_profit_2.py

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        for i in range(1, n):
            if prices[i]>prices[i-1]:
                ans+=(prices[i]-prices[i-1])
        return ans

if __name__=='__main__':
    prices = [7,1,5,3,6,4]
    # prices = [7,6,4,3,1]
    out = Solution().maxProfit(prices)
    print(out)

