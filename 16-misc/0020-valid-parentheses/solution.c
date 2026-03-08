#include <stdbool.h>
#include <string.h>

bool isValid(char* s) {
    int n = strlen(s);
    if (n % 2 != 0) return false; // Odd length can't be valid

    char* stack = (char*)malloc(n);
    int top = -1;

    for (int i = 0; i < n; i++) {
        char c = s[i];
        if (c == '(' || c == '[' || c == '{') {
            stack[++top] = c; // Push
        } else {
            if (top == -1) { free(stack); return false; } // Nothing to match
            
            char topChar = stack[top--]; // Pop
            if ((c == ')' && topChar != '(') ||
                (c == ']' && topChar != '[') ||
                (c == '}' && topChar != '{')) {
                free(stack);
                return false;
            }
        }
    }
    
    bool result = (top == -1);
    free(stack);
    return result;
}

