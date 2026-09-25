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
        queue = deque([])
        Result = []
        Nlist = deque([root])
        queue.append(Nlist)

        while queue:
            Alist = queue.popleft()
            Blist = deque([])
            N = []

            while Alist:
                q = Alist.popleft()
                if q.left:
                    Blist.append(q.left)
                if q.right:
                    Blist.append(q.right)
                
                N.append(q.val)
            Result.append(N)
            if Blist:
                queue.append(Blist)
        return Result
                    

