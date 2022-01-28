#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/27 5:12 下午
# @Author  : xinming
# @File    : 43_multipy_strs.py

class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1=="0" or num2=="0":
            return "0"

        l1, l2 = len(num1), len(num2)
        out = "0"
        for i in range(l1):
            add = 0
            curr = ["0"]*(l1-1-i) # 保存每一个数与另一个完整数相乘的结果,分解补充0字符。
            for j in range(l2-1, -1, -1):
                res = int(num1[i])*int(num2[j]) + add
                y = res%10
                add = res//10
                curr.append(str(y))
            if add >0:
                curr.append(str(add)) # 结束时多一位
            curr_nums = "".join(curr)[::-1]
            out = self.add(out, curr_nums)
        return out

    def add(self, str1, str2):
        i, j = len(str1)-1, len(str2)-1 # 数字的最后一位

        out = []
        add = 0
        while i>=0 or j>=0 or add !=0: #最后一次进的一位不等于0，和就多一位。
            a = int(str1[i]) if i >=0 else 0
            b = int(str2[j]) if j>=0 else 0
            res = a+b+add
            out.append(str(res%10))
            add = res//10
            i-=1
            j-=1
        return "".join(out)[::-1]


if __name__=='__main__':
    str1, str2 = '123', '56789'
    out = Solution().multiply(str1, str2)
    print(out)
