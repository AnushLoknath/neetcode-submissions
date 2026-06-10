

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second=slow.next
        slow.next=None
        pre=None
        while second:
            tmp=second.next
            second.next=pre
            pre=second
            second=tmp
        
        first,second=head,pre
        while second:
            tmp1=first.next
            tmp2=second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2

        