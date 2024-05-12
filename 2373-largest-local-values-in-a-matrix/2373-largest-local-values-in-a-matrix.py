class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def find_max(r,c):
            _max = 0
            
            for nr in range(r,r+3):
                for nc in range(c,c+3):
                    _max = max(_max, grid[nr][nc])
                    
            return _max
                    
        res = []
        
        for r in range(len(grid) - 2):
            row = []
            for c in range(len(grid[0]) - 2):
                row.append(find_max(r,c))
                
            res.append(row)
            
        return res
                
            