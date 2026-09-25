# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def gNodes(root,mVal):
            if not root:
                return 0
            isGood = 1 if root.val >= mVal else 0
            mVal = max (root.val,mVal)
            return isGood + gNodes(root.left,mVal) + gNodes(root.right,mVal)

        return gNodes(root,root.val)

