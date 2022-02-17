#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/16 11:57 上午
# @Author  : xinming
# @File    : 997_find_judge.py

from collections import defaultdict
from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        length = len(trust)
        p = defaultdict(int)
        if length==0 and n==1:
            return n
        for i in range(length):
            a,b = trust[i]
            p[b] = p[b]+1
        for i in range(length):
            a,b = trust[i]
            if a in p.keys():
                p[a] = p[a]-1
        for k, v in p.items():
            if v==n-1:
                return k
        return -1

if __name__=='__main__':
    n=2
    trust=[[1,2],[2,1]]
    out = Solution().findJudge(n=n, trust=trust)
    print(out)