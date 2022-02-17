#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/14 5:29 下午
# @Author  : xinming
# @File    : 297_serialize_deserialize.py

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec_bfs:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return []
        q = deque()
        q.append(root)
        res = ''
        while q:
            node = q.popleft()
            if node != None:
                res += str(node.val) + ','
                q.append(node.left)
                q.append(node.right)
            else:
                res += 'X,'
        return res



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = data.split(',')
        root = TreeNode(data.pop(0))
        q = [root]
        while q:
            node = q.pop(0)
            if data:
                val = data.pop(0)
                if val != 'X':
                    node.left = TreeNode(val)
                    q.append(node.left)
            if data:
                val = data.pop(0)
                if val != 'X':
                    node.right = TreeNode(val)
                    q.append(node.right)
        return root


# Definition for a binary tree node.

# from collections import deque


class Codec_dfs:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return 'X,'
        leftserilized = self.serialize(root.left)
        rightserilized = self.serialize(root.right)
        return str(root.val) + ',' + leftserilized + rightserilized



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        root = self.buildTree(data)
        return root


    def buildTree(self,data):
        val = data.pop(0)
        if val == 'X':
            return None
        node = TreeNode(val)
        node.left = self.buildTree(data)
        node.right = self.buildTree(data)
        return node

if __name__=='__main__':
    root = TreeNode(3)
    root.left=TreeNode(5)
    root.left.left=TreeNode(6)
    root.left.right=TreeNode(2)
    root.left.right.left=TreeNode(7)
    root.left.right.right=TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    p = TreeNode(7)
    q = TreeNode(4)
    ans = Codec_dfs().serialize(root)
    print(ans)
    node = Codec_dfs().deserialize(ans)
    print(node)