class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row, col = 0, len(grid[0]) - 1
        count = 0
        while row < len(grid) and col >= 0:
            if grid[row][col] < 0:
                count += len(grid) - row
                col -= 1
            else:
                row += 1
        return count