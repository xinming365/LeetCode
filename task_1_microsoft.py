#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 4:39 下午
# @Author  : xinming
# @File    : task_1_microsoft.py

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    n = len(S)
    def max_block(S):
        n = len(S)
        max_len = 0
        temp_len = 1
        for i in range(n-1):
            if S[i]==S[i+1]:
                temp_len+=1
            else:
                temp_len = 1
            max_len = max(max_len, temp_len)
        return max_len

    temp_len=1
    max_len = max_block(S)
    sum = 0
    for i in range(n-1):
        tmp = S[i]
        if S[i]==S[i+1]:
            temp_len+=1
        else:
            sum = sum+ (max_len-temp_len)
            temp_len = 1
    sum = sum+ (max_len-temp_len)
    return sum

if __name__=='__main__':

    # my_s = 'babaa'
    # my_s = 'bbbab'
    datas = ['babaa', 'bbbab', "bbbaaabbb"]
    for data in datas:
        out = solution(S=data)
        print(out)