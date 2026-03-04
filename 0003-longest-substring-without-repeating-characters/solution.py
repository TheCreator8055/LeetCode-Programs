class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            if s[r] in char_map and char_map[s[r]] >= l:
                # Move left pointer past the previous occurrence
                l = char_map[s[r]] + 1
            
            char_map[s[r]] = r
            max_len = max(max_len, r - l + 1)
            
        return max_len

