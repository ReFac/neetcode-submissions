# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointA = head
        i = 0
        while pointA and i<n:
            pointA = pointA.next
            i +=1
            
        dummy = ListNode(-1)
        dummy.next = head
        pointT = dummy
        pointB = head
        while pointA:
            pointA =pointA.next
            pointT = pointB
            pointB = pointB.next
        pointT.next = pointB.next
        return dummy.next
        