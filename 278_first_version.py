#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 10:54 上午
# @Author  : xinming
# @File    : 278_first_version.py


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer

bad = 4
def isBadVersion(version):
    FLAGS = True if version >= bad else False
    return FLAGS

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right  = n

        while left <= right:
            mid = (right+left)//2
            if isBadVersion(mid):
                right=mid-1
            else:
                left=mid+1
        return left

if __name__=='__main__':
    out = Solution().firstBadVersion(5)
    print(out)

