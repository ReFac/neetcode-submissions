# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while l1 or l2 or carry ==1:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            Nval= (x+y+carry)%10
            carry = (x+y+carry)//10

            node = ListNode(Nval)
            curr.next=node
            curr = node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
        