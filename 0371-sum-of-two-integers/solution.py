class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        
        # If b > 0, it means there's still a carry to handle for negative numbers
        return (a & mask) if b > 0 else a

