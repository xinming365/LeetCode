#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/12 4:57 下午
# @Author  : xinming
# @File    : 199_right_side_view.py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        right_side=dict()
        stack=[(root,0)]
        max_depth=-1
        while stack:
            node, depth = stack.pop()
            if node is not None:

                if depth not in right_side.keys():
                    right_side[depth]=node.val
                max_depth = max(depth, max_depth)
                if node.left:
                    stack.append((node.left, depth+1))
                if node.right:
                    stack.append((node.right,depth+1))
        out = [right_side[i] for i in range(max_depth+1)]

        return out

class Solution2:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightmost_value_at_depth = dict() # 深度为索引，存放节点的值
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 如果不存在对应深度的节点我们才插入
                rightmost_value_at_depth.setdefault(depth, node.val)

                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]


if __name__=='__main__':
    root = TreeNode(3)
    root.left=TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    ans = Solution().rightSideView(root)
    print(ans)