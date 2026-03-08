class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. Handle the negative exponent case
        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1
        current_product = x
        
        # 2. Binary Exponentiation (Iterative)
        while n > 0:
            # If n is odd, multiply the result by current_product
            if n % 2 == 1:
                res *= current_product
            
            # Square the base and halve the exponent
            current_product *= current_product
            n //= 2
            
        return res

