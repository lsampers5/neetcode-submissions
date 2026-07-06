# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        stack.append((root, float('-inf'), float('inf')))

        while stack:
            current, low, high = stack.pop()
            
            if low < current.val < high: # Checks whether the node is valid based on its own laws and stuff
                if current.right: # look right and add
                    stack.append((current.right, current.val, high))
                if current.left: # look left and add
                    stack.append((current.left, low, current.val))
            else:
                return False
        return True
