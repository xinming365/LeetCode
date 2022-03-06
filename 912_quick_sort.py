#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/2 10:32 上午
# @Author  : xinming
# @File    : 912_quick_sort.py

from typing import List
import random


class Solution2:
    def randomized_partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums

class Solution:
    def sortArray(self, nums):
        def quick_sort(nums, l, r):
            # pivot = nums[random.randint(l, r)]
            pivot = nums[(l+r)//2]
            i, j = l, r
            while i<=j:
                while nums[i]<pivot:
                    i+=1
                while nums[j]>pivot:
                    j-=1
                if i <=j: # the search process may cause i>j.
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
                    j-=1
            if i < r:
                quick_sort(nums, i, r)
            if j > l:
                quick_sort(nums, l, j)

        quick_sort(nums, 0, len(nums)-1)
        return nums


if __name__=='__main__':
    nums=[4,1,5,7,2,6,3,8]
    out = Solution().sortArray(nums=nums)
    print(out)