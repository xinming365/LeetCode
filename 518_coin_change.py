#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 5:10 下午
# @Author  : xinming
# @File    : 518_coin_change.py
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins:
            for j in range(coin, amount+1):
                comb = dp[j]+dp[j-coin]
                dp[j] = comb
        return dp[amount]
if __name__=='__main__':
    amount = 5
    coins = [5, 2, 1]
    out = Solution().change(amount, coins)
    print(out)