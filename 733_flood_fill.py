#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 10:32 下午
# @Author  : xinming
# @File    : 733_flood_fill.py

from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        curr_color = image[sr][sc]
        width = len(image[0])
        height = len(image)

        def dfs(x, y):
            if image[x][y]==curr_color:
                image[x][y]=newColor

            for mx, my in [[x-1, y], [x, y-1], [x+1, y], [x, y+1]]:
                if 0<=mx<height and 0<=my<width and image[mx][my]==curr_color:
                    dfs(mx, my)
        dfs(sr, sc)
        return image

class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        currColor = image[sr][sc]

        def dfs(x: int, y: int):
            if image[x][y] == currColor:
                image[x][y] = newColor
                for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
                        dfs(mx, my)

        if currColor != newColor:
            dfs(sr, sc)
        return image



if __name__=='__main__':
    image = [[0, 0, 0],[0, 0, 0]]
    sr = 0
    sc = 0
    newColor = 2
    out = Solution().floodFill(image, sr, sc, newColor)
    print(out)
