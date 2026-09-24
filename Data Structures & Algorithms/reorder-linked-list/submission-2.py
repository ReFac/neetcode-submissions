# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        nxt = slow.next
        slow.next = None

        prev = None
        curr = nxt
        while curr:
            nt = curr.next
            curr.next = prev
            prev = curr
            curr = nt
        
        dummy = ListNode(-1,head)
        p1,p2=head,prev
        while p2:
            p1_nxt = p1.next
            p2_nxt = p2.next

            p1.next = p2
            p2.next = p1_nxt

            p1 = p1_nxt
            p2 = p2_nxt

            
            

        

        
# 3,5,7
# 2,3,4
        

        