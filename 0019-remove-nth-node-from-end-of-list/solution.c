/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    // 1. Create a dummy node to handle edge cases (like removing the head)
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    if (!dummy) return head; 

    dummy->next = head;
    struct ListNode *fast = dummy;
    struct ListNode *slow = dummy;

    // 2. Advance fast pointer so that the gap between fast and slow is n nodes
    for (int i = 0; i <= n; i++) {
        fast = fast->next;
    }

    // 3. Move both pointers until fast reaches the end
    while (fast != NULL) {
        fast = fast->next;
        slow = slow->next;
    }

    // 4. slow->next is the node to be removed
    struct ListNode* nodeToDelete = slow->next;
    slow->next = slow->next->next;
    free(nodeToDelete);

    // 5. Save the new head and free the dummy node
    struct ListNode* newHead = dummy->next;
    free(dummy);
    
    return newHead;
}

