class Solution:
    def dfs(self,row, col, board):
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        inbound = lambda r,c: -1 < r < len(board) and -1 < c < len(board[0])
        count = 0

        if board[row][col] == "M":
            board[row][col] = "X"
            return

        for row_change, col_change in DIR:
            new_row = row + row_change
            new_col = col + col_change

            if inbound(new_row, new_col) and board[new_row][new_col] == "M":
                count += 1
        if count > 0:
            board[row][col] = str(count)
            return

        board[row][col] = "B"

        for row_change, col_change in DIR:
            new_row = row + row_change
            new_col = col + col_change
            if inbound(new_row, new_col)  and board[new_row][new_col] == "E":
                    self.dfs(new_row, new_col, board)
                        
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.dfs(click[0], click[1], board)
        return board