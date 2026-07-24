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
     * @return {number[][]}
     */
    levelOrder(root) {
        if (root == null) {
            return [];
        }
        
        const bfs = [];
        const queue = [];

        queue.push({node: root, depth: 0});

        let pointer = 0;

        while (pointer < queue.length) {
            const el = queue[pointer];
            pointer++;

            bfs.push(el);

            if (el.node.left != null) queue.push({node: el.node.left, depth: el.depth + 1});
            if (el.node.right != null) queue.push({node: el.node.right, depth: el.depth + 1});
        }

        const result = [];
        let currentDepth = 0;
        for (let node of bfs) {
            if (node.depth >= currentDepth) {
                result.push([])
                currentDepth++;
            }
            result[node.depth].push(node.node.val)
        }

        return result;
    }
}
