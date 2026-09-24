"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        clones = {None: None}

        def get_clone(node: 'Optional[Node]') -> 'Optional[Node]':
            if node not in clones:
                clones[node] = Node(node.val)
            return clones[node]

        curr = head
        while curr:
            copy = get_clone(curr)
            copy.next = get_clone(curr.next)
            copy.random = get_clone(curr.random)
            curr = curr.next

        return clones[head]

