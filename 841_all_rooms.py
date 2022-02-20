#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/17 12:16 下午
# @Author  : xinming
# @File    : 841_all_rooms.py

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        stack = [0]
        while stack:
            room_index = stack.pop()
            for key in rooms[room_index]:
                if key not in visited:
                    visited.add(key)
                    

