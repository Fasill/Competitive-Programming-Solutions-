# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odds = head
        evens = head.next
        e = evens
        while evens and evens.next:
            odds.next = evens.next
            odds = odds.next
            evens.next = odds.next
            evens = evens.next
        odds.next = e
        return head