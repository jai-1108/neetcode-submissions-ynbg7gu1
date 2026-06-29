# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        p1, p2 = 1
        p1 = 2, n=1
        p1 = 3, n=0

        p1 = 4, p2 = 2
        p2.next = p2.next.next, so from 2->3->4 to 2->4



        """
        
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        while n:
            fast = fast.next
            n-=1
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
