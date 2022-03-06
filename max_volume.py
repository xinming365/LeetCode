#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/5 11:09 上午
# @Author  : xinming
# @File    : max_volume.py

def read_input():
    a = input('the size is : ')
    b = input('the direction is ')
    c = input('the distance is ' )
    def convert(str):
        l = str.split(' ')
        l = [int(i) for i in l]
        return l
    return convert(a), b.split(' '),convert(c)


def max_volume():
    # a, b, c = read_input()
    a, b, c = [2, 3], ['x', 'y', 'z'], [1, 1, 1]
    size, ncuts = a
    directions = b
    cuts = c

    def find_i_cuts(i):
        # i=0, 1, 2, 3,...
        ncuts = i+1
        x_cuts, y_cuts, z_cuts = [], [], []
        for i in range(ncuts):
            if directions[i]=='x':
                x_cuts.append(cuts[i])
            if directions[i]=='y':
                y_cuts.append(cuts[i])
            if directions[i]=='z':
                z_cuts.append(cuts[i])
        return x_cuts, y_cuts, z_cuts

    def find_max_volume_ith(i):
        # i=0, 1, 2, 3,...
        def find_max(i_cuts):
            max_i = 0
            len_i = len(i_cuts)
            for i in range(1, len_i):
                max_i = max(max_i, i_cuts[i]-i_cuts[i-1])
            max_i = max(max_i, i_cuts[0] , size - i_cuts[len_i - 1])
            return max_i
        x_cuts, y_cuts, z_cuts = find_i_cuts(i)
        height, width, depth = size, size, size
        if x_cuts:
            width = find_max(x_cuts[:i+1])
        if y_cuts:
            height = find_max(y_cuts[:i+1])
        if z_cuts:
            depth = find_max(z_cuts[:i+1])
        return height*width*depth

    for i in range(ncuts):
        print(find_max_volume_ith(i))
    # return None

if __name__=='__main__':
    out = max_volume()
    print(out)