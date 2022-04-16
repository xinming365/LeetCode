#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 12:42 下午
# @Author  : xinming
# @File    : 797_all_path.py

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        stack = []

        def dfs(x):
            if x==len(graph)-1:
                ans.append(stack[:])
                return None

            for y in graph[x]:
                stack.append(y)
                dfs(y)
                stack.pop()
        stack.append(0)
        dfs(0)
        return ans

if __name__=='__main__':
    graph = [[1,2],[3],[3],[]]
    ans = Solution().allPathsSourceTarget(graph=graph)
    print(ans)
