#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 10:55 上午
# @Author  : xinming
# @File    : 130_solve.py

from collections import deque
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        queue = deque()

        m = len(board)
        n = len(board[0])

        for row in range(m):
            if board[row][0]=='O':
                queue.append((row, 0))
                board[row][0]='A'
            if board[row][n-1]=='O':
                queue.append((row, n-1))
                board[row][n-1]='A'

        for col in range(n):
            if board[0][col]=='O':
                queue.append((0, col))
                board[0][col]='A'
            if board[m-1][col]=='O':
                queue.append((m-1, col))
                board[m-1][col]='A'

        while queue:
            x, y = queue.popleft()
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0<=nx<m and 0<=ny<n and board[nx][ny]=='O':
                    board[nx][ny]='A'
                    queue.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if board[i][j]=='A':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
        return board
if __name__=='__main__':
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    out = Solution().solve(board=board)
    print(out)
