class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(row,col):
            if board[row][col] == "X":
                return
            
            visited.add((row,col))
            for direction in DIR:
                new_row, new_col = row + direction[0], col + direction[1]
                
                if (new_row, new_col) not in visited and in_bound(new_row, new_col):
                    dfs(new_row, new_col)
        
        visited = set()
        DIR = [[1,0],[0,1],[-1,0],[0,-1]]
        in_bound = lambda row, col: 0 <= row < len(board) and 0 <= col < len(board[row])
        
        #checking  the top and bottom side of the board to find "O"s that are on the border 
        # or have connetion with "O" on the border 
        for i in range(len(board[0])):
            dfs(0,i)
            dfs(len(board) - 1,i)
            
        #checking the 1st row and last row   
        for j in range(len(board)):
            dfs(j,0)
            dfs(j,len(board[j]) - 1)
            
        #flipping "O"s that are not on the border and not connected to an 'O'on the border
        for rw in range(len(board)):
            for cl in range(len(board[rw])):
                if (rw,cl) not in visited:
                       board[rw][cl] = "X"
        