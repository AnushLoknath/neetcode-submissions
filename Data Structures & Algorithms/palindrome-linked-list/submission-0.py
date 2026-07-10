# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow
        slow=None
        pre=None
        while second:
            tmp=second.next
            second.next=pre
            pre=second
            second=tmp

        first=head
        second=pre
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True
        