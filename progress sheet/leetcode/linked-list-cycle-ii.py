# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        "BFS"
        '''
        _set = set()
        cur = head
        while cur:
            if cur in _set:
                return cur
            else:_set.add(cur)
            cur = cur.next
        '''
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head
         