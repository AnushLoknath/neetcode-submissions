

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        r= head
        l=dummy
    
        while n>0 and r:
            r=r.next
            n-=1
        while r:
            l=l.next
            r=r.next
        l.next=l.next.next
        return dummy.next


        