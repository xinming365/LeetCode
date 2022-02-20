#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/17 11:44 上午
# @Author  : xinming
# @File    : 1557_find_smallest_set.py

from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        endSet = set(y for x, y in edges)
        ans = [i for i in range(n) if i not in endSet]
        return ans

