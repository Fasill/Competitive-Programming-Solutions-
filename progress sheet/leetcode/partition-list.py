# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # cur = head
        # while cur:
        #     if cur.val<=x:
        #         newnode = ListNode(cur.val)
        #         newnode.next = head
        #         head = newnode
        #         if cur.next:
        #             cur.val = cur.next.val
        #             cur.next = cur.next.next
        #         else:
        #             cur = None

        #     cur = cur.next
        # return head
        dummiy1  = ListNode(0)
        d1= dummiy1
        dummiy2  = ListNode(0)
        d2= dummiy2

        cur = head
        while cur:
            newnode = ListNode(cur.val)
            if cur.val <x:
                 d1.next = newnode
                 d1 = d1.next
            else:
                 d2.next = newnode
                 d2 = d2.next

            cur = cur.next

        d1.next = dummiy2.next
        return dummiy1.next
