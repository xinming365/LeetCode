#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/24 10:44 上午
# @Author  : xinming
# @File    : 79_exist.py

from typing import List
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         m = len(board)
#         n = len(board[0])
#
#         def bfs(r, c, d):
#             # if len(word)==0:
#             #     return True
#             if word[0]!=board[r][c]:
#                 return False
#             for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
#                 if 0<=i<m and 0<=j<n and  board[i][j]==word[d+1]:
#                     tmp = board[i][j]
#                     print('{} in {}'.format(tmp, word))
#                     d = d+1
#                     bfs(r, c, d)
#
#                 else:
#                     if d==len(word):
#                         return True
#
#
#         for r in range(m):
#             for c in range(n):
#                 if  bfs(r, c, 0):
#                     return True
#         return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 使用深度优先搜索
        if not board:   # 边界条件
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0: # 如果单词已经检查完毕
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:  # 如果路径出界或者矩阵中的值不是word的首字母，返回False
            return False
        tmp = board[i][j]  # 如果找到了第一个字母，检查剩余的部分
        board[i][j] = '0'
        res = self.dfs(board,i+1,j,word[1:]) or self.dfs(board,i-1,j,word[1:]) or self.dfs(board,i,j+1,word[1:]) or self.dfs(board, i, j-1, word[1:]) # 上下左右四个方向搜索

        board[i][j] = tmp  # 标记过的点恢复原状，以便进行下一次搜索
        return res


if __name__=='__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    out = Solution().exist(board, word)
    print(out)
