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
     * @param {number} k
     * @return {number}
     */
    kthSmallest(root, k) {
        return this.findOrder(root)[k - 1].val; 
    }

    findOrder(root) {
        if (root == null) return []; 
        return [...this.findOrder(root.left), root, ...this.findOrder(root.right)]
    }
}
