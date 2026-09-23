# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS, at each elvel, we need to check which is most right, so basically the latest element per level of the BFS
        result = []

        if not root:
            return []

        frontier = [root]

        while len(frontier) > 0:
            new_front = []
            current = frontier[0]
            for el in frontier:
                if el:
                    if el.left:
                        new_front.append(el.left)
                    if el.right:
                        new_front.append(el.right)
                    current = el.val

            result.append(current)
            frontier = new_front


        return result
        