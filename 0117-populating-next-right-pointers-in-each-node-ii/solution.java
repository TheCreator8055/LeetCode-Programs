class Solution {
    public Node connect(Node root) {
        Node head = root; // Head of the current level
        
        while (head != null) {
            Node dummy = new Node(0); // Dummy node for the next level
            Node tail = dummy; // Tail to build the next level linked list
            
            // Traverse current level using next pointers
            for (Node cur = head; cur != null; cur = cur.next) {
                if (cur.left != null) {
                    tail.next = cur.left;
                    tail = tail.next;
                }
                if (cur.right != null) {
                    tail.next = cur.right;
                    tail = tail.next;
                }
            }
            // Move down to the start of the next level
            head = dummy.next;
        }
        return root;
    }
}

