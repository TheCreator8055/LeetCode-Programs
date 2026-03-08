class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow case for 32-bit integers
        MAX, MIN = 2**31 - 1, -2**31
        if dividend == MIN and divisor == -1: return MAX
        
        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        res = 0
        
        # Exponential subtraction (Bit Shifting)
        for i in range(31, -1, -1):
            if (a >> i) >= b:
                res += (1 << i)
                a -= (b << i)
        
        return -res if negative else res

