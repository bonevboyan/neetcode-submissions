# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        modTree = root

        if not root:
            return 0

        count = 0

        q = deque([root])
        qMaxValue = deque([root.val])

        while q:
            el = q.popleft()
            maxValueUntilNow = qMaxValue.popleft()

            if not el:
                continue

            
            q.append(el.left)
            q.append(el.right)

            if el.val >= maxValueUntilNow:
                count = count + 1

            maxValLeft = maxValueUntilNow
            if el.left and el.left.val >= maxValueUntilNow:
                maxValLeft = el.left.val

            maxValRight = maxValueUntilNow
            if el.right and el.right.val >= maxValueUntilNow:
                maxValRight = el.right.val

            qMaxValue.append(maxValLeft)
            qMaxValue.append(maxValRight)

        return count

            


            

        


