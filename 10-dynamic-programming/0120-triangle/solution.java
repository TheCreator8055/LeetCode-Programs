import java.util.List;

class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[] dp = new int[n];
        
        // Initialize DP array with the bottom row values
        for (int i = 0; i < n; i++) {
            dp[i] = triangle.get(n - 1).get(i);
        }
        
        // Bottom-up DP optimization
        for (int row = n - 2; row >= 0; row--) {
            for (int col = 0; col <= row; col++) {
                // Choice: minimum of the two adjacent children + current node value
                dp[col] = Math.min(dp[col], dp[col + 1]) + triangle.get(row).get(col);
            }
        }
        return dp[0];
    }
}

