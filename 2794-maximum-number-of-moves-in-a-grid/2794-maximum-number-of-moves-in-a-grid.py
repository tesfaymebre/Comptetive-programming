class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        max_Moves, total_Rows, total_Columns = 0, len(grid), len(grid[0])
        cache = {} 
        
        directions = [(-1, 1), (0, 1), (1, 1)]

        def traverse(row: int, column: int, prev_No: int = -1):
            if (row < 0 or row >= total_Rows or 
                column < 0 or column >= total_Columns or 
                grid[row][column] <= prev_No):
                return 0  
            
            if (row, column) not in cache:
                best_Choice = 0  

                for dr, dc in directions:
                    best_Choice = max(best_Choice, traverse(row + dr, column + dc, grid[row][column]))
                
                cache[(row, column)] = 1 + best_Choice 
            
            return cache[(row, column)]

        for row in range(total_Rows):
            max_Moves = max(max_Moves, traverse(row, 0))

        return max_Moves - 1 if max_Moves != 0 else 0