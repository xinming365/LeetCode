#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/5 10:32 上午
# @Author  : xinming
# @File    : max_sub_meituan02.py


def read_input():
    n = input('the length of the list: ')
    l = input('the list is ')
    n=int(n)
    l = l.split(' ')
    l = [int(i) for i in l]
    return n, l

def max_sub():
    length, my_list = read_input()
    max_sum=0
    ans = 0
    pre_sum=[]
    sum=0
    for i in range(length):
        max_sum += my_list[i]
        if max_sum<0:
            max_sum=0
        ans = max(ans, max_sum)
        sum+=my_list[i]
        pre_sum.append(sum)

if __name__=='__main__':
    out = read_input()
    print(out)

