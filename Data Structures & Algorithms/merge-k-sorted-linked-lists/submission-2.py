# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """

        """
        array = []
        
        for li in lists:
            while li:
                array.append(li.val)
                li = li.next
        array.sort()
        dummy = ListNode()
        curr = dummy
        for n in array:
            curr.next = ListNode(n)
            curr = curr.next
        return dummy.next
