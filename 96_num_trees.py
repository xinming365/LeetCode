#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/21 10:51 上午
# @Author  : xinming
# @File    : 96_num_trees.py

class Solution:
    def numTrees(self, n: int) -> int:
        if n==0:
            return 1
        G = [0 for i in range(n+1)]
        G[0]=1
        for i in range(1, n+1):
            for j in range(i):

                G[i] += G[j] * G[i-j-1]
        return G[n]

if __name__=='__main__':
    out = Solution().numTrees(3)
    print(out)
