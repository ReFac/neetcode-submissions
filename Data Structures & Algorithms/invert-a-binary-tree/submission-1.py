# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            r = queue.popleft()
            r.left,r.right = r.right,r.left
            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)

        return root
            

        