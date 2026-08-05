class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def gain_from_subtree(node):
            if not node:
                return 0
                
            # Drop negative gains by taking max with 0
            left_gain = max(gain_from_subtree(node.left), 0)
            right_gain = max(gain_from_subtree(node.right), 0)
            
            # Current node acts as the highest turn-around point of the path
            current_path_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return max single-branch gain to the parent node
            return node.val + max(left_gain, right_gain)
            
        gain_from_subtree(root)
        return self.max_sum

