#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/17 11:52 上午
# @Author  : xinming
# @File    : 714_max_profit.py
from typing import List
class Solution2:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = prices[0] + fee
        profit = 0
        for i in range(1, n):
            # 之后考虑手续费的影响
            if prices[i]+fee<buy:
                buy=prices[i]+fee
            elif prices[i]>buy:
                profit += (prices[i]-buy)
                buy=prices[i]
        return profit

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp[i][0]: 没有股票最大利润
        # dp[i][1]: 有股票最大利润

        n = len(prices)
        dp = [[0 for i in range(2)] for i in range(n)]

        dp[0][0]=0
        dp[0][1]=-prices[0]

        for i in range(1, n):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
            dp[i][1]= max(dp[i-1][0]-prices[i], dp[i-1][1])
        return  dp[n-1][0]

if __name__=='__main__':
    prices = [1,3,7,5,10,3]
    out = Solution2().maxProfit(prices=prices, fee=3)
    print(out)
