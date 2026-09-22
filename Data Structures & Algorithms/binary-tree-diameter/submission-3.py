# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1
# |
# 2

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0;

        left = root.left
        right = root.right

        return max(self.height(left) + self.height(right), 
            self.diameterOfBinaryTree(left), 
            self.diameterOfBinaryTree(right))

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0;

        left = root.left
        right = root.right

        return max(self.height(left), self.height(right)) + 1
        