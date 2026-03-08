class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findBound(isFirst):
            low, high, ans = 0, len(nums) - 1, -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    ans = mid
                    if isFirst: high = mid - 1 # Keep looking left
                    else: low = mid + 1      # Keep looking right
                elif nums[mid] < target: low = mid + 1
                else: high = mid - 1
            return ans
        
        return [findBound(True), findBound(False)]

