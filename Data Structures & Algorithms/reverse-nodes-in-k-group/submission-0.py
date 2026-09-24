# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverseK(p: Optional[ListNode], head: Optional[ListNode], k: int) -> Optional[ListNode]:
            n = k
            prev = None
            curr = head
            while curr and k > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k -= 1
            
            p.next = prev
            head.next =curr

            return curr

        def check(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return k <1
        
        dummy = ListNode(-1,head)
        prev = dummy
        curr = head
        while curr:
            c1 = check(curr,k)
            if c1:
                node = reverseK(prev,curr,k)
                prev = curr
                curr = node
            else:
                break
        return dummy.next


            

            

        


        

        