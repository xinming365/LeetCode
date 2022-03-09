#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/8 8:25 下午
# @Author  : xinming
# @File    : 62_uniq_paths.py

class Solution2:
    def uniquePaths(self, m:int, n:int) ->int:
        f = [[0 for i in range(n)] for i in range(m)]
        # 递归的初始条件。转移方程需要处理好初始条件。
        for i in range(n):
            f[0][i]=1
        for i in range(m):
            f[i][0]=1
        # 从上方或者左方转移过来。
        for i in range(1, m):
            for j in range(1, n):
                f[i][j]=f[i][j-1] +f[i-1][j]
        return f[m-1][n-1]

class Solution(object):
    def uniquePaths(self, m, n):
        # 用哈希表存储，减少计算量
        d = {}
        def dfs(i,j):
            # 从缓存中直接读取
            if (i,j) in d:
                return d[i,j]
            # 到达边界后只有一条路
            if i==m-1 or j==n-1:
                return 1
            d[i,j] = dfs(i+1, j)+ dfs(i,j+1)
            return d[i,j]
        return dfs(0, 0)


if __name__=='__main__':
    out = Solution().uniquePaths(3, 7)
    print(out)