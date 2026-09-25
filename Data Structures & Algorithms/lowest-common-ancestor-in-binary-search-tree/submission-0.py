# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        
        c1 = self.lowestCommonAncestor(root.left,p,q)
        c2 = self.lowestCommonAncestor(root.right,p,q)

        if c1 and c2:
            return root
        elif c1:
            return c1
        elif c2:
            return c2
        else:
            return None


        
