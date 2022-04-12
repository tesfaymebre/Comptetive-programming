class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        in_bound = lambda row,col: 0 <= row < len(board) and 0 <= col < len(board[row])
        DIR = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                count = 0
                curr_val = board[i][j]
                
                for x,y in DIR:
                    new_r, new_c = i + x, j + y
                    if in_bound(new_r, new_c) and abs(board[new_r][new_c]) == 1:
                        count += 1
                if board[i][j] == 1:
                    if count < 2 or count > 3:   
                        board[i][j] = -1
                else:
                    if count == 3:  
                        board[i][j] = 2
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
        