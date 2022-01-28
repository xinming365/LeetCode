#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/27 7:18 下午
# @Author  : xinming
# @File    : 187_find_repeat_DNA.py
from typing import List
from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = len(s)
        L=10
        dict_dna = defaultdict(int) #
        # 例如11个A，遍历两次。
        for i in range(l-L+1):
            dict_dna[s[i:i+L]]+=1
        out = []
        for k, v in dict_dna.items():
            if v>1:
                out.append(k)
        return out


if __name__=='__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    out = Solution().findRepeatedDnaSequences(s)
    print(out)
