# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Step 1 I am going to do a inorder traversal 
        # Left - Node - Right
        orderedNodes = []

        def inOrder (node):
            if not node:
                return
            else:
                inOrder(node.left)
                orderedNodes.append(node.val)
                inOrder(node.right)
        
        inOrder(root)
 
        return orderedNodes[k - 1] # return the kth element
                