class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def backtrack(remain, stack, start):
            if remain == 0:
                res.append(list(stack))
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= remain:
                    stack.append(candidates[i])
                    # Note: i stays the same because we can reuse the element
                    backtrack(remain - candidates[i], stack, i)
                    stack.pop()
        backtrack(target, [], 0)
        return res

