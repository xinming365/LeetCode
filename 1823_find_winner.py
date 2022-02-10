#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/10 12:10 上午
# @Author  : xinming
# @File    : 1823_find_winner.py

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        s, Q = 0, [i for i in range(1, n + 1)]
        while len(Q) > 1:
            lost = (s + k - 1) % len(Q)    #确定该轮失败者的位置
            s = lost if (lost != len(Q) - 1) else 0   #更新下一轮开始的人
            del Q[lost]   #删除失败者
        return Q[0]


if __name__=='__main__':
    a = Solution().findTheWinner(5,2)
    print(a)