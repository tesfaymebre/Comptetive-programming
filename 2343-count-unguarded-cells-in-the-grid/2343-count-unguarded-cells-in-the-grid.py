class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        seen = set((x,y) for x,y in guards + walls)
        guarded_cells = 0
        visited = set()
        
        in_bound = lambda row,col: 0 <= row < m and 0 <= col < n
        DIR = [(1,0),(0,1),(-1,0),(0,-1)]
        
        for x,y in guards:
            
            for d in DIR:
                cur_x,cur_y = x, y
                cur_x,cur_y = cur_x + d[0], cur_y + d[1] 
                
                while in_bound(cur_x,cur_y) and (cur_x,cur_y) not in seen:
                    if (cur_x,cur_y) not in visited:
                        guarded_cells += 1
                        visited.add((cur_x,cur_y))
                        
                    cur_x,cur_y = cur_x + d[0], cur_y + d[1]  

        return(n*m - len(seen) - guarded_cells)