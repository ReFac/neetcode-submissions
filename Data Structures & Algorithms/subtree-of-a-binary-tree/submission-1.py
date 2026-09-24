# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree (p,q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                c1 = isSameTree(p.left,q.left)
                c2 = isSameTree(p.right,q.right)
                return c1 and c2
            else:
                return False

        if not root:
            return False
        elif not subRoot:
            return False
        
        queue = deque([root])
        while queue:
            q = queue.popleft()
            if q.val == subRoot.val:
                c = isSameTree(q,subRoot)
                if c:
                    return c
            if q.left:
                queue.append(q.left)
            if q.right:
                queue.append(q.right)
        
        return False
                
        