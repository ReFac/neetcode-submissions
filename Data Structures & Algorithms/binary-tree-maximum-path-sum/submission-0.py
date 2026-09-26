# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxM = float('-inf')
        def helper(root):
            if not root:
                return 0
            val = root.val
            left = max(helper(root.left),0)
            right = max(helper(root.right),0)
            self.maxM= max(val + left + right, self.maxM)
            return (max(left,right)+val)
        helper(root)
        return self.maxM
        