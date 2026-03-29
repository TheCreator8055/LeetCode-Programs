class Solution:
    def grayCode(self, n: int) -> list[int]:
        # Using the standard mathematical formula: G(i) = i ^ (i >> 1)
        res = []
        for i in range(1 << n): # 1 << n is 2^n
            res.append(i ^ (i >> 1))
        return res

