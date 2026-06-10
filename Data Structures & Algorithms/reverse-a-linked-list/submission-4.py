
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        pre=None
        while curr:
            nxt=curr.next
            curr.next=pre
            pre=curr
            curr=nxt
        return pre
       
    
      

        