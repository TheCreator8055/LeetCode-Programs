class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode curr = head;
        int count = 0;
        while (count < k && curr != null) { // Check if we have k nodes
            curr = curr.next;
            count++;
        }
        if (count == k) {
            curr = reverseKGroup(curr, k); // Get the head of the reversed next group
            while (count-- > 0) { // Standard reversal
                ListNode temp = head.next;
                head.next = curr;
                curr = head;
                head = temp;
            }
            head = curr;
        }
        return head;
    }
}

