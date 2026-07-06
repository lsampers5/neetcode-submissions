# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
# Adjusted plan of attack
# We are going to do a in order traversal but just count and compare with k to stop early
        count = 0
        result = None

        def inOrder (node):
            nonlocal result, count

            if not node:
                return
            else:
                inOrder(node.left)
                count += 1
                if k == count:
                    result = node.val
                    return
                inOrder(node.right)
        
        inOrder(root)
        return result
                