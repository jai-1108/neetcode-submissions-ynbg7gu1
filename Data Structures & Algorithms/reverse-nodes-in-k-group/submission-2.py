class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        slow = head
        
        # Check if there are at least k nodes left
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            return head

        fast = head
        # Move fast to the k-th node
        for _ in range(k - 1):
            fast = fast.next
        
        next_head = fast.next
        fast.next = None
        
        new_head = self.reverseLL(head)
        # After reverseLL, 'head' is now the tail of the reversed segment
        head.next = self.reverseKGroup(next_head, k)
        
        return new_head
        

    def reverseLL(self, head: Optional[ListNode]):
        if not head:
            return None
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev