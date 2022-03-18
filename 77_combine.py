#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/18 10:36 上午
# @Author  : xinming
# @File    : 77_combine.py
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path=[]
        if k<=0 or n<k:
            return res

        def back_track(start_index):
            if len(path)==k:
                res.append(path[:])
                return None

            for i in range(start_index, n+1):
                path.append(i)
                back_track(i+1)
                path.pop()
        back_track(1)
        return res

if __name__=='__main__':
    out = Solution().combine(1, 1)
    print(out)






