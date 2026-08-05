#include <string>
#include <cctype>

class Solution {
public:
    bool isPalindrome(std::string s) {
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            // Skip invalid non-alphanumeric entries from left
            while (left < right && !std::isalnum(s[left])) {
                left++;
            }
            // Skip invalid non-alphanumeric entries from right
            while (left < right && !std::isalnum(s[right])) {
                right--;
            }
            
            // Core equality comparison step
            if (std::tolower(s[left]) != std::tolower(s[right])) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};

