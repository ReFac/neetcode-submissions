# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        queue = deque([(p,q)])
        while queue:
            (i,j) = queue.popleft()
            if not i and not j:
                continue
            elif i and j and i.val == j.val:
                queue.append((i.left,j.left))
                queue.append((i.right,j.right))
            else:
                return False
        
        return True