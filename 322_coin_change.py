#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 4:45 下午
# @Author  : xinming
# @File    : 322_coin_change.py
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

if __name__=='__main__':
    coins = [1, 2, 5]
    amount = 11
    out = Solution().coinChange(coins=coins, amount=amount)
    print(out)