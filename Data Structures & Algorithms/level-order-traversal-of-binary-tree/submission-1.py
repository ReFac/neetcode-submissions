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
        Result = []
        while queue:
            level_Size = len(queue)
            Nlist = []
            for _ in range(level_Size):
                n = queue.popleft()
                if n.left:
                    queue.append(n.left) 
                if n.right:
                    queue.append(n.right)
                Nlist.append(n.val)
            Result.append(Nlist)
        return Result
