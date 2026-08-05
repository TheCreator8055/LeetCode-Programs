class Solution {
public:
    Node* connect(Node* root) {
        if (!root) return nullptr;
        
        Node* leftMost = root;
        
        // Loop down the left boundary of the perfect tree
        while (leftMost->left) {
            Node* head = leftMost;
            
            while (head) {
                // Connection 1: children under the same parent
                head->left->next = head->right;
                
                // Connection 2: children between adjacent parent nodes
                if (head->next) {
                    head->right->next = head->next->left;
                }
                
                head = head->next;
            }
            leftMost = leftMost->left;
        }
        
        return root;
    }
};

