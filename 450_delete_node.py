#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/13 1:48 下午
# @Author  : xinming
# @File    : 450_delete_node.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def predecessor(self, root):
        """
        左子树的最大值，满足二叉搜素数条件的节点。适用于右子树不存在的根结点。
        :param root: 根节点
        :return:
        """
        if not root:
            return None
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def successor(self, root):
        """
        右子树的最小值。适用于只有右子树，和左右子树都存在的情况。
        BST的性质保证了其大于原始根结点(root)左子树的值，且其必然小于root.right.
        :param root:
        :return:
        """
        if not root:
            return None
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        递归删除找到替换的节点，并递归删除这个值
        :param root:
        :param key:
        :return:
        """
        if not root:
            return None
        if key < root.val:
            # 此处调用递归函数。更新root.left
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 找到叶子节点，直接删掉。
            if not root.left and not root.right:
                root=None
            elif not root.right:
                # 不改变二叉树的连接关系，替换掉这个值
                root.val = self.predecessor(root)
                # 删除predecessor
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)

        return root






if __name__=='__main__':
    root = TreeNode(3)
    root.left=TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(23)
    ans = Solution().deleteNode(root, 23)
    print(ans)