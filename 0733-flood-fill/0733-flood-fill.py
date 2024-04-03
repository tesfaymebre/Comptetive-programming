class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.color_start = image[sr][sc]
        
        if self.color_start == color:
            return image
        
        DIR = [[1,0],[0,1],[-1,0],[0,-1]]
        inbound = lambda r,c : -1 < r < len(image) and -1 < c < len(image[0])
        
        def dfs(r,c):
            image[r][c] = color
            
            for x,y in DIR:
                nr = r + x
                nc = c + y
                
                if inbound(nr,nc) and image[nr][nc] == self.color_start:
                    dfs(nr,nc)
                    
            return
        
        dfs(sr,sc)
        return image
        