#include <stdlib.h>
#include <string.h>

// Comparison function for qsort
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

void backtrack(int* nums, int numsSize, int** res, int* returnSize, int* current, int* visited, int depth) {
    if (depth == numsSize) {
        res[*returnSize] = (int*)malloc(numsSize * sizeof(int));
        memcpy(res[*returnSize], current, numsSize * sizeof(int));
        (*returnSize)++;
        return;
    }

    for (int i = 0; i < numsSize; i++) {
        // Skip if already used
        if (visited[i]) continue;

        // SKIP DUPLICATES: 
        // If current element is same as previous AND previous wasn't used in this path
        if (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1]) continue;

        visited[i] = 1;
        current[depth] = nums[i];
        backtrack(nums, numsSize, res, returnSize, current, visited, depth + 1);
        
        // Backtrack
        visited[i] = 0;
    }
}

int** permuteUnique(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    // 1. Sort to bring duplicates together
    qsort(nums, numsSize, sizeof(int), compare);

    // 2. Allocate worst-case memory (n!)
    int maxTotal = 1;
    for (int i = 1; i <= numsSize; i++) maxTotal *= i;
    
    int** res = (int**)malloc(maxTotal * sizeof(int*));
    int* current = (int*)malloc(numsSize * sizeof(int));
    int* visited = (int*)calloc(numsSize, sizeof(int));
    *returnSize = 0;

    // 3. Start Backtracking
    backtrack(nums, numsSize, res, returnSize, current, visited, 0);

    // 4. Fill returnColumnSizes
    *returnColumnSizes = (int*)malloc((*returnSize) * sizeof(int));
    for (int i = 0; i < *returnSize; i++) {
        (*returnColumnSizes)[i] = numsSize;
    }

    // Clean up temp arrays
    free(current);
    free(visited);

    return res;
}

