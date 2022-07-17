class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        seen = [] + guards + walls
        seen = set((x,y) for x,y in seen)
        in_bound = lambda row,col: 0 <= row < m and 0 <= col < n
        
        guarded_cells = 0
        visited = set()
        
        for x,y in guards:
            cur_x,cur_y = x, y
            cur_x += 1 
            while in_bound(cur_x,cur_y) and (cur_x,cur_y) not in seen:
                if (cur_x,cur_y) not in visited:
                    guarded_cells += 1
                    
                visited.add((cur_x,cur_y))
                cur_x += 1 
                
            cur_x,cur_y = x, y
            cur_x -= 1
            while in_bound(cur_x,cur_y) and (cur_x,cur_y) not in seen:
                if (cur_x,cur_y) not in visited:
                    guarded_cells += 1
                    
                visited.add((cur_x,cur_y))
                cur_x -= 1 
        
            cur_x,cur_y = x, y
            cur_y += 1
            while in_bound(cur_x,cur_y) and (cur_x,cur_y) not in seen: 
                if (cur_x,cur_y) not in visited:
                    guarded_cells += 1
                    
                visited.add((cur_x,cur_y))
                cur_y += 1
                
            cur_x,cur_y = x, y
            cur_y -= 1
            while in_bound(cur_x,cur_y) and (cur_x,cur_y) not in seen:
                if (cur_x,cur_y) not in visited:
                    guarded_cells += 1
                    
                visited.add((cur_x,cur_y))
                cur_y -= 1 
                       
        return(n*m - len(seen) - guarded_cells)