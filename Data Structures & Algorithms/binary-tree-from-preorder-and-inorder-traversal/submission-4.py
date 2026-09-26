# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {val : i for i, val in enumerate(inorder)}
        self.size = len(preorder)
        pre_iter = iter(preorder)
        def helper(left,right):
            if left > right:
                return None
            rt_val = next(pre_iter)
            mid = index_map[rt_val]
            root = TreeNode(val = rt_val)
            
            root.left = helper(left,mid-1)
            root.right = helper(mid+1,right)

            return root

        return helper(0,self.size-1)
        