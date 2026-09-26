# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        res = []
        queue = deque([root])
        while queue:
            note = queue.popleft()
            res.append(str(note.val)if note else "#")
            if note:
                queue.append(note.left)
                queue.append(note.right)
        return ",".join(res)





        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        datas = data.split(",")
        root = TreeNode(int(datas[0]))
        queue = deque([root])
        i = 1
        n = len(datas)
        while queue and i < n:
            par = queue.popleft()
            if datas[i] != "#":
                note = TreeNode(int(datas[i]))
                queue.append(note)
                par.left = note
            i +=1

            if i < n and datas[i] != "#":
                note = TreeNode(int(datas[i]))
                queue.append(note)
                par.right = note
            i +=1
        return root

        
