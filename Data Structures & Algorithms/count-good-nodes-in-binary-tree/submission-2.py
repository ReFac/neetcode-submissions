# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good(root,maxv):
            res = 0
            if not root:
                return 0
            if root.val >= maxv:
                maxv = root.val
                res = 1
            left = good(root.left,maxv)
            right = good(root.right,maxv)
            return res+left+right
        return good(root,float("-inf"))
                
            
