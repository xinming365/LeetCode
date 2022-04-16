#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/11 10:20 上午
# @Author  : xinming
# @File    : 39_combination_sum.py

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        # candidates.sort()
        res = []
        def back_track(idx, combinations, comb_sum):
            if comb_sum==target:
                res.append(combinations)
                return None
            if comb_sum>target or idx>=n:
                return None

            back_track(idx, combinations+ [candidates[idx]], comb_sum+candidates[idx])
            back_track(idx+1, combinations , comb_sum)
        back_track(0, [], 0)
        return res



class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        n = len(candidates)
        res = []
        def helper(idx, tmp_sum, combine):
            if tmp_sum > target or idx == n:
                return
            if tmp_sum == target:
                res.append(combine)
                return
            print('Before, temporary sum is {}'.format(tmp_sum + candidates[idx]))
            print('temporary candidates are {}'.format(combine + [candidates[idx]]))
            helper(idx, tmp_sum + candidates[idx], combine + [candidates[idx]])
            # print('After, temporary sum is {}'.format(tmp_sum + candidates[i]))
            # print('temporary candidates are {}'.format(tmp + [candidates[i]]))
            helper(idx + 1, tmp_sum, combine)
        helper(0, 0, [])
        return res

if __name__=='__main__':
    candidates = [2,3,6,7]
    target = 7
    out = Solution().combinationSum(candidates, target)
    print(out)