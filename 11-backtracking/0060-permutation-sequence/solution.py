import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        res = []
        k -= 1  # Convert to 0-indexed
        
        while n > 0:
            n -= 1
            # Determine which "block" of permutations k falls into
            index, k = divmod(k, math.factorial(n))
            res.append(numbers.pop(index))
            
        return "".join(res)

