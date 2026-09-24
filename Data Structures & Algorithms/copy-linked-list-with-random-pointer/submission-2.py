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
        if not head:
            return None
        curr =head
        while curr:
            nxt = curr.next
            copy = Node(curr.val,nxt)
            curr.next = copy
            curr = curr.next.next
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        result = head.next
        while curr:
            copy = curr.next
            curr.next = curr.next.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        return result

