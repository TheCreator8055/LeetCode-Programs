class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs: return ""
        # Take the first word as the reference
        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                # If index exceeds word length or characters don't match
                if i == len(word) or word[i] != base[i]:
                    return base[:i]
        return base

