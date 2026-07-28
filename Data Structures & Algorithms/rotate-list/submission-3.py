# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        k=k%len(arr)
        arr[:]=arr[-k:]+arr[:-k]
        
        curr=head
        for i in range(len(arr)):
            curr.val=arr[i]
            curr=curr.next
        return head

        
        