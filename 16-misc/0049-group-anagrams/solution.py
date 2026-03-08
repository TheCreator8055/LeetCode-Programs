from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 1. Use a dictionary where the key is the sorted string
        # and the value is a list of its anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 2. Sort the string to create a unique key
            # "eat" -> ('a', 'e', 't')
            key = "".join(sorted(s))
            
            # 3. Add the original string to the corresponding group
            anagram_map[key].append(s)
            
        # 4. Return just the grouped lists
        return list(anagram_map.values())

