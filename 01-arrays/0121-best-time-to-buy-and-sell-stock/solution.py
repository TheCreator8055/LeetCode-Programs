class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Track lowest buying price seen so far
            if price < min_price:
                min_price = price
            # Calculate potential profit if sold today
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

