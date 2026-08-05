class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            val = postorder.pop()
            root = TreeNode(val)
            
            index = inorder_map[val]
            
            # Right subtree must be built first because postorder processes Root after Right
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)

