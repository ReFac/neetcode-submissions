# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root,upper,lower):
            if not root:
                return True
            elif lower<root.val < upper:
                c1 = bst(root.left,root.val,lower)
                c2 = bst(root.right,upper,root.val)
                return c1 and c2
            else:
                return False

        return bst(root,float("inf"),float("-inf"))

            
            
                
                
        