#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/3 4:29 下午
# @Author  : xinming
# @File    : microsoft_test.py

def three_sum(input, target):
    length = len(input)
    for i in range(length):
        for j in range(i, length):
            diff = target-input[i]-input[j]
            res = input[j:]
            if diff in res:
                k = res.index(diff)
                return [i, j, k]

def improve_three_sum(input, target):
     input.sort()
     length = len(input)
     right = length-1
     for i in range(length-1):
         diff = target-input[i]
         left = i+1
         while left<right:
            lv = input[left]
            rv = input[right]
            if (lv+rv)< diff:
                left+=1
            if (lv+rv)>diff:
                right-=1
            if (lv+rv)==diff:
                return [i, left, right]



if __name__=='__main__':
    input = [1,4,5,67,7,8]
    target = 10
    out = improve_three_sum(input, target)
    print(out)