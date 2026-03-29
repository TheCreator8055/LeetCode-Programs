#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void backtrack(int row, int n, int* cols, int* d1, int* d2, char** board, char*** res, int* resSize) {
    if (row == n) {
        // Correctly allocating a new 2D board for the results array
        res[*resSize] = (char**)malloc(n * sizeof(char*));
        for (int i = 0; i < n; i++) {
            res[*resSize][i] = strdup(board[i]);
        }
        (*resSize)++;
        return;
    }

    for (int col = 0; col < n; col++) {
        // d1: row + col is constant for anti-diagonals
        // d2: row - col + n is constant for main diagonals
        if (!cols[col] && !d1[row + col] && !d2[row - col + n]) {
            board[row][col] = 'Q';
            cols[col] = d1[row + col] = d2[row - col + n] = 1;
            
            backtrack(row + 1, n, cols, d1, d2, board, res, resSize);
            
            // Backtrack
            board[row][col] = '.';
            cols[col] = d1[row + col] = d2[row - col + n] = 0;
        }
    }
}

char*** solveNQueens(int n, int* returnSize, int** returnColumnSizes) {
    *returnSize = 0;
    // Pre-allocating max possible solutions (approximate for n=9)
    char*** res = (char***)malloc(1000 * sizeof(char**));
    
    // Initialize empty board
    char** board = (char**)malloc(n * sizeof(char*));
    for (int i = 0; i < n; i++) {
        board[i] = (char*)malloc((n + 1) * sizeof(char));
        memset(board[i], '.', n);
        board[i][n] = '\0';
    }

    int *cols = calloc(n, sizeof(int));
    int *d1 = calloc(2 * n, sizeof(int));
    int *d2 = calloc(2 * n, sizeof(int));

    backtrack(0, n, cols, d1, d2, board, res, returnSize);

    // LeetCode requirement: set the size for each board in the result
    *returnColumnSizes = (int*)malloc((*returnSize) * sizeof(int));
    for (int i = 0; i < *returnSize; i++) (*returnColumnSizes)[i] = n;

    // Free temporary memory
    for (int i = 0; i < n; i++) free(board[i]);
    free(board); free(cols); free(d1); free(d2);

    return res;
}
// 
