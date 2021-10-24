"""
Link: https://leetcode.com/problems/count-complete-tree-nodes/

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:

Input: root = []
Output: 0
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        if root is None:
            return self.count

        if root.val is not None:
            self.count += 1

        if root.left is not None:
            self.__incrementAndCount(root.left)

        if root.right is not None:
            self.__incrementAndCount(root.right)

        return self.count

    def __incrementAndCount(self, node: Optional[TreeNode]):
        self.count += 1
        self.__countNodes(node)

    def __countNodes(self, root: Optional[TreeNode]):
        if root.left is not None:
            self.__incrementAndCount(root.left)

        if root.right is not None:
            self.__incrementAndCount(root.right)

"""
RESULT

Runtime: 145 ms, faster than 9.57% of Python3 online submissions for Count Complete Tree Nodes.
Memory Usage: 21.6 MB, less than 57.82% of Python3 online submissions for Count Complete Tree Nodes.
"""
