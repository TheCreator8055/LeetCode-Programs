class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
            
        # Fast and slow pointers to find the middle elements
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # Disconnect the left half of the list
        if prev:
            prev.next = None
            
        root = TreeNode(slow.val)
        
        # Recursively build subtrees
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        
        return root

