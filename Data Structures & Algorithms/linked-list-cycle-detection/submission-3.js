/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {boolean}
     */
    hasCycle(head) {
        if (head == null) return false;
        if (head.next == null) return false;

        const set = new Set();

        let iterator = head;
        set.add(iterator);

        while (iterator.next != null) {
            if (set.has(iterator.next)) {
                return true;
            }
            iterator = iterator.next;
            set.add(iterator);
        }

        return false;
    }
}
