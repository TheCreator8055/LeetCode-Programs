class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Python's string 'find' returns the index or -1 if not found
        # Alternatively, using a loop:
        n, h = len(needle), len(haystack)
        for i in range(h - n + 1):
            if haystack[i : i + n] == needle:
                return i
        return -1

