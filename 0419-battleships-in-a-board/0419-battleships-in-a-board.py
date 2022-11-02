class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        inbound = lambda r,c: 0 <= r < len(board) and 0 <= c < len(board[0])
        count = 0
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    if inbound(r,c-1) and board[r][c-1] != 'X' and inbound(r-1,c) and board[r-1][c] != 'X':
                        count += 1
                    elif c == 0 and (not inbound(r-1,c) or board[r-1][c] != 'X'):
                        count += 1
                    elif r == 0 and (not inbound(r,c-1) or board[r][c-1] != 'X'):
                        count += 1
                    
        return count