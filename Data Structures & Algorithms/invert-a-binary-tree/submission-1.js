/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {TreeNode}
     */
    invertTree(root) {
        if (root == null) {
            return root;
        }

        const newRight = this.invertTree(root.left)
        const newLeft = this.invertTree(root.right)

        return new TreeNode(root.val, newLeft, newRight);
    }
}
