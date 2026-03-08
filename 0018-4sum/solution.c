#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int** fourSum(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes) {
    qsort(nums, numsSize, sizeof(int), compare);
    int** res = (int**)malloc(1000 * sizeof(int*)); // Arbitrary initial size
    *returnColumnSizes = (int*)malloc(1000 * sizeof(int));
    *returnSize = 0;

    for (int i = 0; i < numsSize - 3; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue; // Skip duplicates for i
        for (int j = i + 1; j < numsSize - 2; j++) {
            if (j > i + 1 && nums[j] == nums[j - 1]) continue; // Skip duplicates for j
            
            int left = j + 1, right = numsSize - 1;
            while (left < right) {
                long sum = (long)nums[i] + nums[j] + nums[left] + nums[right];
                if (sum == target) {
                    res[*returnSize] = (int*)malloc(4 * sizeof(int));
                    res[*returnSize][0] = nums[i];
                    res[*returnSize][1] = nums[j];
                    res[*returnSize][2] = nums[left];
                    res[*returnSize][3] = nums[right];
                    (*returnColumnSizes)[*returnSize] = 4;
                    (*returnSize)++;
                    
                    while (left < right && nums[left] == nums[left + 1]) left++; // Skip duplicates
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++; right--;
                } else if (sum < target) left++;
                else right--;
            }
        }
    }
    return res;
}

