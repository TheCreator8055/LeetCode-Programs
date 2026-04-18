class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            # Area = width * height of the shorter side
            current_water = (right - left) * min(height[left], height[right])
            max_water = max(max_water, current_water)
            
            # Move the pointer of the shorter wall to seek a taller one
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water

