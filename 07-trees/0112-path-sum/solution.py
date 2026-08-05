class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # Check if it is a leaf node
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursively check subtrees with reduced sum
        new_sum = targetSum - root.val
        return self.hasPathSum(root.left, new_sum) or self.hasPathSum(root.right, new_sum)

