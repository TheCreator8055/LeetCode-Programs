class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort() # Sort to handle duplicates easily
        res = []
        def backtrack(remain, stack, start):
            if remain == 0:
                res.append(list(stack))
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue # Skip same element to avoid duplicate combinations
                if candidates[i] > remain: break # Optimization
                
                stack.append(candidates[i])
                backtrack(remain - candidates[i], stack, i + 1)
                stack.pop()
        backtrack(target, [], 0)
        return res

