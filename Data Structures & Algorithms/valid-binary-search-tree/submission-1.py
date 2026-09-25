# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root,lower,upper):
            if not root:
                return True
            if upper <= root.val or lower >= root.val:
                return False
            
            c1 = isValid(root.left, lower,root.val)
            c2 = isValid(root.right, root.val, upper)
            return c1 and c2
        upper = float("inf")
        lower = -float("inf")
        return isValid(root,lower,upper)
                
                
        