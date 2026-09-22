# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        fast = head
        slow = head
        check = False
        while slow.next:
            slow = slow.next
            if fast.next:
                if fast.next.next:
                    fast = fast.next.next
                else:
                    return False
            else:
                return False

            if slow == fast:
                return True
                break
        return False
            
        