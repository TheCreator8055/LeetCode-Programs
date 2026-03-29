class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort() # Sort to keep duplicates together
        res = []
        
        def backtrack(start, path):
            res.append(list(path))
            for i in range(start, len(nums)):
                # If current element is same as previous, skip to avoid duplicate subsets
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(0, [])
        return res

