class Solution {
    public void setZeroes(int[][] matrix) {
        boolean firstCol = false;
        int R = matrix.length, C = matrix[0].length;
        for (int i = 0; i < R; i++) {
            if (matrix[i][0] == 0) firstCol = true;
            for (int j = 1; j < C; j++) 
                if (matrix[i][j] == 0) { matrix[i][0] = 0; matrix[0][j] = 0; }
        }
        for (int i = R - 1; i >= 0; i--) {
            for (int j = C - 1; j >= 1; j--)
                if (matrix[i][0] == 0 || matrix[0][j] == 0) matrix[i][j] = 0;
            if (firstCol) matrix[i][0] = 0;
        }
    }
}

