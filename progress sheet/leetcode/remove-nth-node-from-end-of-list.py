# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        n = length-n
        cur = head
        if n == 0:
            return head.next
        
        while n>1:
            cur = cur.next
            n -= 1
        
        cur.next = cur.next.next

        return head        