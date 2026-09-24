# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            c1 = self.isSameTree(p.left,q.left)
            c2 = self.isSameTree(p.right,q.right) 
            return c1 and c2

        else:
            return False
        