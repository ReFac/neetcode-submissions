# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preI, self.inI = 0,0
        size = len(preorder)
        def helper(limit):
            if self.preI >= size:
                return None
            if inorder[self.inI] == limit:
                self.inI +=1
                return None
            rtVal = preorder[self.preI]
            root = TreeNode(rtVal)
            self.preI +=1
            root.left =  helper(rtVal)
            root.right = helper(limit)
            return root
        return helper(float("inf"))

        

        