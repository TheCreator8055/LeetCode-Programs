class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Trim trailing spaces and split into words
        words = s.strip().split()
        return len(words[-1]) if words else 0

