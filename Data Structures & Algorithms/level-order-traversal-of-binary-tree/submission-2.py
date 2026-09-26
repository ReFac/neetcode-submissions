# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            size = len(queue)
            r = []
            for _ in range(size):
                note = queue.popleft()
                r.append(note.val)
                if note.left:
                    queue.append(note.left)
                if note.right:
                    queue.append(note.right)
            res.append(r)
        
        return res
                

                

