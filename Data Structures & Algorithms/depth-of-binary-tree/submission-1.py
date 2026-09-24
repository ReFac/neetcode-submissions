# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                q = queue.popleft()
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            depth +=1
        return depth
            
        