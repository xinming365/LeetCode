#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/9 2:03 下午
# @Author  : xinming
# @File    : 1249_remove_brackets.py

def minRemoveToMakeValid(s: str) -> str:
    indexes_to_remove = set()
    stack = []
    for i, c in enumerate(s):
        if c not in "()":
            continue
        if c == "(":
            stack.append(i)
        elif not stack:
            indexes_to_remove.add(i)
        else:
            stack.pop()
    indexes_to_remove = indexes_to_remove.union(set(stack))
    string_builder = []
    for i, c in enumerate(s):
        if i not in indexes_to_remove:
            string_builder.append(c)
    return "".join(string_builder)

if __name__=='__main__':
    s = 'lee(t(c)o)de)'
    out = minRemoveToMakeValid(s)