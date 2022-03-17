#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 8:34 下午
# @Author  : xinming
# @File    : 121_max_profit.py
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        init_price = prices[0]
        max_profit = 0
        for i in range(1, n):
            max_profit = max(prices[i]-init_price, max_profit)
            init_price = min(init_price, prices[i])
        return max_profit if max_profit>0 else 0

if __name__=='__main__':
    prices = [7,1,5,3,6,4]
    prices = [7,6,4,3,1]
    out = Solution().maxProfit(prices)
    print(out)
