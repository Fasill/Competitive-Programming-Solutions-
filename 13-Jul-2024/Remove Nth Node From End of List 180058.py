# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        leng = 0
        cur = head
        while cur:
            cur = cur.next
            leng+=1
        if leng == n:
            head = head.next
            return head
        leng -= n
        cur = head
        while leng> 1:
            cur = cur.next
            leng -= 1
        print(cur)
        if cur.next:
            cur.next = cur.next.next
        
        return head
