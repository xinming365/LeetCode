#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/26 8:27 下午
# @Author  : xinming
# @File    : 1314_matrix_block_sum.py

from typing import List
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        cols = len(mat[0])
        rows = len(mat)

        res = [[0 for i in range(cols)] for i in range(rows)]

        pre = [[0 for i in range(cols+1)] for i in range(rows+1)]
        # 二维数组的前缀和，注意在最左侧和最上方补充上0元素。
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                pre[i][j]=pre[i-1][j]+pre[i][j-1]-pre[i-1][j-1]+mat[i-1][j-1]

        for r in range(rows):
            for c in range(cols):
                rkp, ckp = r+k+1, c+k+1
                rkm, ckm = r-k, c-k
                if rkm<0: rkm=0
                if ckm<0: ckm=0
                if rkp>rows: rkp=rows
                if ckp>cols: ckp=cols

                res[r][c]=pre[rkp][ckp]-pre[rkm][ckp]-pre[rkp][ckm]+pre[rkm][ckm]
        return res

if __name__=='__main__':
    # mat = [[1,2,4,3],[5,1,2,4],[6,3,5,9]]
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    out = Solution().matrixBlockSum(mat=mat, k=k)
    print(out)