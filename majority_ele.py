#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 11:00 下午
# @Author  : xinming
# @File    : majority_ele.py

from typing import List
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict={}

        for i in nums:
            if i not in num_dict:
                num_dict[i]=1
            else:
                num_dict[i] +=1
        mid_lens = math.floor(len(num_dict)/2)
        for k, v in num_dict.items():
            if v > mid_lens:
                return k


if __name__=='__main__':
    s =[3,2,3]
    out = Solution().majorityElement(s)
    print(out)
