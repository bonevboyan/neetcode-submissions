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
     * @return {boolean}
     */
    // isValidBST(root) {
    //     if (root == null || (root.left == null && root.right == null)) {
    //         return true;
    //     }
    //     if (root.left == null && root.right != null) {
    //         return (root.val < root.right.val) && this.isValidBST(root.right);
    //     }
    //     if (root.right == null && root.left != null) {
    //         return root.left.val < root.val && this.isValidBST(root.left);
    //     }

    //     if (root.left.val < root.val && root.right.val > root.val) {
    //         return this.isValidBST(root.left) && this.isValidBST(root.right);
    //     } else {
    //         return false;
    //     }
    // }

    isValidBST(root, min = -Infinity, max = Infinity) {
        if (root == null) return true;

        if (root.val <= min || root.val >= max) {
            return false;
        }

        return this.isValidBST(root.left, min, root.val) &&
            this.isValidBST(root.right, root.val, max);
    }
}
