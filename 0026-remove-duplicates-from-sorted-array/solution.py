class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums: return 0
        
        # 'write_index' tracks where the next unique element should go
        write_index = 1 
        
        for i in range(1, len(nums)):
            # If current element is different from the previous one, it's unique
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
                
        return write_index

