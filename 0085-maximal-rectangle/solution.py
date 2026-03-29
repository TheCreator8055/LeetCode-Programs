class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])
        # heights stores the height of '1's for each column
        heights = [0] * n
        max_area = 0
        
        for row in matrix:
            for i in range(n):
                # If current cell is '1', add to previous height, else reset to 0
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            # For every row, calculate the max rectangle using the updated heights
            max_area = max(max_area, self.largestRectangleArea(heights))
            
        return max_area

    def largestRectangleArea(self, heights: list[int]) -> int:
        # Helper function using a Monotonic Stack (from Problem 84)
        stack = [-1] # Initialize with -1 to handle width calculation easily
        max_a = 0
        # Add a 0 at the end to ensure all bars are popped at the end
        h_copy = heights + [0]
        
        for i in range(len(h_copy)):
            while h_copy[i] < h_copy[stack[-1]]:
                height = h_copy[stack.pop()]
                # width = current index - new top index - 1
                width = i - stack[-1] - 1
                max_a = max(max_a, height * width)
            stack.append(i)
            
        return max_a

