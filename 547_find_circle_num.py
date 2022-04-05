#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/5 11:16 下午
# @Author  : xinming
# @File    : 547_find_circle_num.py

from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            for j in range(n):
                if isConnected[i][j]==1 and j not in visited:
                    visited.add(j)
                    dfs(j)


        n = len(isConnected)
        res = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i)
                res+=1
        return res


if __name__=='__main__':
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    out = Solution().findCircleNum(isConnected=isConnected)
    print(out)