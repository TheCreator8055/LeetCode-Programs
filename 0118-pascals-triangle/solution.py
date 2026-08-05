class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            # Create a row filled with 1s
            row = [1] * (row_num + 1)
            
            # Fill the inner elements of the row
            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
                
            triangle.append(row)

        return triangle

