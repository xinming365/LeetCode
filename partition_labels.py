#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/26 12:56 下午
# @Author  : xinming
# @File    : partition_labels.py
from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict_c={}
        for i, c in enumerate(s): # 哈希字典统计字符出现的最远位置。
            dict_c[c]=i
        current_max = 0
        start = 0
        out = []
        for i, c in enumerate(s):
            if dict_c[c]>current_max:
                current_max = dict_c[c] #维护当前每个字符出现的最远位置。
            if i==current_max: # 当迭代到跟最远相等时，结束。不得不找的最大片段，保证片段数最多，
                end = i
                out.append(end-start+1)
                start=end+1
        return out


if __name__=='__main__':
    s="ababcbacadefegdehijhklij"
    out = Solution().partitionLabels(s)
    print(out)