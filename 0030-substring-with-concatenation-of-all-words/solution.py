from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words: return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        res = []
        
        # Sliding window across possible starting points
        for i in range(len(s) - total_len + 1):
            # Extract the current window
            current_window = s[i : i + total_len]
            # Split the window into chunks of word_len
            seen_words = []
            for j in range(0, total_len, word_len):
                seen_words.append(current_window[j : j + word_len])
            
            # Compare frequencies
            if Counter(seen_words) == word_count:
                res.append(i)
                
        return res

