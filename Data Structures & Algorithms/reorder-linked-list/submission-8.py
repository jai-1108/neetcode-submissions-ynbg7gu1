# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        fast = fast.next.next
        slow = slow.next

        slow = 0, fast = 0
        slow = 1, fast = 2
        slow = 2, fast = 4
        slow= 3, fast = 6

        from 0 to 3, list1, 0->1->2->3
        from 3 to 6, list2
        reverse list2, 6->5->4

        0->6->1->5->2->4->3
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list2 = slow.next
        prev = None 
        slow.next = None
        while list2:
            tmp = list2.next
            list2.next = prev
            prev = list2
            list2 = tmp
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

            

    
        