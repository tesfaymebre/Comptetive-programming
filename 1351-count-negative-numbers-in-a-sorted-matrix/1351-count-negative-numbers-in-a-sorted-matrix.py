class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            left = 0
            right = len(grid[i]) - 1
            while left <= right:
                mid = left + (right - left)//2
                if grid[i][mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            count += len(grid[i]) - right - 1
        return count