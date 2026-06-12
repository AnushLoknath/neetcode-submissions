
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head and left== right:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        for i in range(left-1):
            pre=pre.next
        curr=pre.next
        prenode=None
        for i in range(right-left+1):
            tmp=curr.next
            curr.next=prenode
            prenode=curr
            curr=tmp
        pre.next.next=curr
        pre.next=prenode
        return dummy.next
    
      