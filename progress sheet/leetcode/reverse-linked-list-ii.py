# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left -= 1
        right += 1
        start = dummy
        end = dummy
        while right:
            if left:
                start = start.next
                left -= 1
            end= end.next
            right -= 1

        prev = end
        reverse = start.next
        while reverse != end and reverse:
            hold = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = hold
        start.next = prev
        return dummy.next

