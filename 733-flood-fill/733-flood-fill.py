class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        
        def dfs(i, j):
            image[i][j] = newColor
            visited.add((i,j))
            
            for direction in DIR:
                new_row, new_column = i + direction[0], j + direction[1]
                if (new_row, new_column) in visited or not in_bound(new_row, new_column) or \
                    image[new_row][new_column] != start_color:
                    continue
                
                dfs(new_row, new_column)
                
        in_bound = lambda i, j : 0 <= i < len(image) and 0 <= j < len(image[0])
        
        visited = set()
        start_color = image[sr][sc]
        DIR = [[0,-1],[1,0],[0,1],[-1,0]]
        
        dfs(sr,sc)
        
        return image
                    