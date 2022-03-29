#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 12:32 上午
# @Author  : xinming
# @File    : 713_subarray_products.py

from typing import List
from functools import reduce

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #同样排除k为1的情况比如  [1,1,1] k=1
        """
        k=100
        位置i：    0,  1, 2, 3
        数组nums： 10, 5, 2, 6
        窗口1(r=2)：   l, r
        窗口1(r=3):    l,    r

        窗口1中符合的有[5],[2],[5,2]
        窗口2中符合的有[5],[2],[5,2],[6],[2,6],[5,2,6]
        可以看出，
        窗口2对比窗口1多出来的数组都是由于窗口右滑一次所带来的，即多出来的那几个必然是包含新窗口的边界r的

        因此可以得出，最终答案可以是每次窗口最大长度的累加。
        """
        if k<=1:
            return 0
        left, right = 0, 0
        #创建一个变量记录路上的乘积
        product = 1
        #记录连续数组的组合个数
        ans = 0

        #用右指针遍历整个数组，每次循环右指针右移一次
        while right<len(nums):
            product *= nums[right]

            while product>=k:
                product/=nums[left]
                left+=1
            ans +=right-left+1
            right+=1
        return ans


class Solution2:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        res = []
        for i in range(1, n+1):
            window = [0 for _ in range(i)]
            for j in range(i):
                window[j]=nums[j]
            product = reduce(lambda x, y: x*y, window)
            if product<k:
                res.append(window[:])
            for j in range(n-i):
                window.pop(0)
                window.append(nums[j+i])
                product = reduce(lambda x, y: x*y, window)
                if product<k:
                        res.append(window[:])
        return len(res)
if __name__=='__main__':
    nums = [10,5,2,6]
    k = 100
    out = Solution().numSubarrayProductLessThanK(nums=nums, k=k)
    print(out)

