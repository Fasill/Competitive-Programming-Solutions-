# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n+=1
        

        fast = head
        slow = head
        st = []
        while fast and fast.next:
            st.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        if n%2 != 0:
            slow = slow.next
        while slow:
            if slow.val == st[-1]:
                st.pop()
                slow = slow.next
            else:
                return False

        return True