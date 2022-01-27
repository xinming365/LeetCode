#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/27 11:25 上午
# @Author  : xinming
# @File    : 49_group_anagrams.py
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out=[]
        sorted_dict={}
        for i in strs:
            ch_list = sorted(i)
            keys="".join(ch_list)
            if keys not in sorted_dict.keys():
                sorted_dict[keys]=[]

            sorted_dict[keys].append(i)
        for k, v in sorted_dict.items():
            out.append(v)
        # list(sorted_dict.values()) 更加简洁。
        return out

if __name__=='__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    out = Solution().groupAnagrams(strs)
    print(out)


