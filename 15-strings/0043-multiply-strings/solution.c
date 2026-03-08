char* multiply(char* num1, char* num2) {
    int n1 = strlen(num1), n2 = strlen(num2);
    if (num1[0] == '0' || num2[0] == '0') return "0";
    
    int* res = (int*)calloc(n1 + n2, sizeof(int));
    for (int i = n1 - 1; i >= 0; i--) {
        for (int j = n2 - 1; j >= 0; j--) {
            int mul = (num1[i] - '0') * (num2[j] - '0');
            int sum = mul + res[i + j + 1];
            res[i + j + 1] = sum % 10;
            res[i + j] += sum / 10;
        }
    }

    // 1. Determine where the actual digits start (skip leading zero if it exists)
    int start = (res[0] == 0) ? 1 : 0;
    int resLen = n1 + n2 - start;

    // 2. Allocate memory for the return string (+1 for null terminator)
    char* resultStr = (char*)malloc((resLen + 1) * sizeof(char));
    
    for (int i = 0; i < resLen; i++) {
        resultStr[i] = res[i + start] + '0';
    }
    resultStr[resLen] = '\0';

    // 3. Free the temporary integer array and return the string
    free(res);
    return resultStr;
}

