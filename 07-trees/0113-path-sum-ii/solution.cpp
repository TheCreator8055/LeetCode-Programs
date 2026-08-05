#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> pathSum(TreeNode* root, int targetSum) {
        std::vector<std::vector<int>> result;
        std::vector<int> currentPath;
        findPaths(root, targetSum, currentPath, result);
        return result;
    }

private:
    void findPaths(TreeNode* node, int targetSum, std::vector<int>& currentPath, std::vector<std::vector<int>>& result) {
        if (!node) return;

        currentPath.push_back(node->val);

        if (!node->left && !node->right && targetSum == node->val) {
            result.push_back(currentPath);
        } else {
            findPaths(node->left, targetSum - node->val, currentPath, result);
            findPaths(node->right, targetSum - node->val, currentPath, result);
        }

        currentPath.pop_back(); // Backtrack
    }
};

