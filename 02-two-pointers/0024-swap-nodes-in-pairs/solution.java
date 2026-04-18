class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;
        
        ListNode first = head;
        ListNode second = head.next;
        
        // Swapping logic
        first.next = swapPairs(second.next);
        second.next = first;
        
        return second; // New head of the pair
    }
}

