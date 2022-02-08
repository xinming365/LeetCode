#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/8 2:08 下午
# @Author  : xinming
# @File    : 155_min_stack.py
import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]