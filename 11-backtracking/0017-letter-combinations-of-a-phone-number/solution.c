#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* phoneMap[] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

void backtrack(char* digits, int index, char* current, char** res, int* resSize) {
    if (digits[index] == '\0') {
        res[*resSize] = strdup(current);
        (*resSize)++;
        return;
    }
    char* letters = phoneMap[digits[index] - '0'];
    for (int i = 0; letters[i] != '\0'; i++) {
        current[index] = letters[i];
        current[index + 1] = '\0'; // Ensure string is null-terminated
        backtrack(digits, index + 1, current, res, resSize);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** letterCombinations(char* digits, int* returnSize) {
    *returnSize = 0;
    int len = strlen(digits);
    if (len == 0) return NULL;

    // 1. Calculate total combinations for malloc
    int total = 1;
    for (int i = 0; i < len; i++) {
        total *= strlen(phoneMap[digits[i] - '0']);
    }

    // 2. Allocate memory for the result array and temporary buffer
    char** res = (char**)malloc(total * sizeof(char*));
    char* current = (char*)malloc((len + 1) * sizeof(char));
    
    // 3. Start backtracking
    backtrack(digits, 0, current, res, returnSize);

    free(current);
    return res;
}

