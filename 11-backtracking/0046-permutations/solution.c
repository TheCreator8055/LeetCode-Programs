#include <stdlib.h>
#include <string.h>

/**
 * Helper function to perform backtracking swaps.
 */
void backtrack(int* nums, int numsSize, int first, int** res, int* returnSize) {
    if (first == numsSize) {
        // Allocate space for this specific permutation and copy current state
        res[*returnSize] = (int*)malloc(numsSize * sizeof(int));
        memcpy(res[*returnSize], nums, numsSize * sizeof(int));
        (*returnSize)++;
        return;
    }
    
    for (int i = first; i < numsSize; i++) {
        // Swap: Move element i to the "first" position
        int tmp = nums[first]; 
        nums[first] = nums[i]; 
        nums[i] = tmp;
        
        backtrack(nums, numsSize, first + 1, res, returnSize);
        
        // Backtrack: Swap back to restore original state
        tmp = nums[first]; 
        nums[first] = nums[i]; 
        nums[i] = tmp;
    }
}

/**
 * Main entry point for LeetCode.
 * Note: Both returned array and *columnSizes array must be malloced.
 */
int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    // 1. Calculate n! to know how much memory to allocate
    int total = 1;
    for (int i = 1; i <= numsSize; i++) {
        total *= i;
    }

    // 2. Allocate the result array (array of int pointers)
    int** res = (int**)malloc(total * sizeof(int*));
    *returnSize = 0;

    // 3. Start the recursion
    backtrack(nums, numsSize, 0, res, returnSize);

    // 4. Fill returnColumnSizes (each permutation has numsSize elements)
    *returnColumnSizes = (int*)malloc(total * sizeof(int));
    for (int i = 0; i < total; i++) {
        (*returnColumnSizes)[i] = numsSize;
    }

    return res;
}

