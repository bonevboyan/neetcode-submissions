class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        self.height(root)
        return self.best

    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left = self.height(node.left)
        right = self.height(node.right)

        if left + right > self.best:
            self.best = left + right

        if left > right:
            return left + 1
        return right + 1