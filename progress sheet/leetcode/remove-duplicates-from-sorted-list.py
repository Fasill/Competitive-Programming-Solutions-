# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        _set = set()
        while cur:
            if cur.val in _set:
                prev.next = cur.next
            else:
                _set.add(cur.val)
                prev = cur
            cur = cur.next
        return head
        