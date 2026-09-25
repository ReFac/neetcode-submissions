# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        self.check = k
        self.val = root.val
        
        def kth(root):
            if root.left:
                kth(root.left)
            if self.check >0:
                self.val = root.val
                self.check -= 1
            if root.right:
                kth(root.right)
        kth(root)
        return self.val