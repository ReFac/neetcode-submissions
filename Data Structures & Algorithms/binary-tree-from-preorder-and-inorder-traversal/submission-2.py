# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # 1. 前序遍历的第一个元素为根节点
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 2. 找到根节点在中序遍历中的索引
        mid = inorder.index(root_val)
        
        # 3. 递归构建左右子树
        # 左子树节点数量为 mid
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        return root