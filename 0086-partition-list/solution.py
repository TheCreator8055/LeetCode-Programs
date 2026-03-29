class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes to start two separate lists
        before_head = ListNode(0)
        after_head = ListNode(0)
        before = before_head
        after = after_head
        
        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next
        
        # Connect the end of 'before' list to the start of 'after' list
        after.next = None # Important: avoid cycles
        before.next = after_head.next
        
        return before_head.next

