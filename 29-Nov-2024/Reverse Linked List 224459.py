# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        cur = head
        while cur:
            fut = cur.next
            cur.next = prev
            prev = cur
            cur = fut
        return prev