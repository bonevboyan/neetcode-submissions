# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> int:
        self.bal = True
        self.height(root)
        return self.bal

    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left = self.height(node.left)
        right = self.height(node.right)

        if left > right + 1 or right > left + 1:
            self.bal = False

        if left > right:
            return left + 1
        return right + 1


        