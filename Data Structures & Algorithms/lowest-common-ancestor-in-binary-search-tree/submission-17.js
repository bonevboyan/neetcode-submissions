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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {TreeNode}
     */
    lowestCommonAncestor(root, p, q) {
        const n = root.val;
        const pVal = p.val;
        const qVal = q.val;


        if (pVal > n && qVal > n) {
            return this.lowestCommonAncestor(root.right, p, q);
        } else if (pVal < n && qVal < n) {
            return this.lowestCommonAncestor(root.left, p, q);
        } else {
            return root;
        }
    }
}
