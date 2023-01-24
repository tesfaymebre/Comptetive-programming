class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board_2 = [0]
        rows, cols = len(board), len(board[0])
        row = rows - 1

        while row>=0:
            for col in range(cols):
                board_2.append(board[row][col])
            row -= 1
            if row >= 0:
                for col in range(cols-1, -1, -1):
                    board_2.append(board[row][col])
                row -= 1

        visited = [0 for i in range(len(board_2))]
        stack = collections.deque()
        
        stack.append([1,0])
        while stack:
            curr_ind, curr_dist = stack.popleft()
            for i in range(1,7):
                next_ind = min(rows*cols,curr_ind + i)
                if board_2[next_ind] != -1:
                    next_ind = board_2[next_ind]
                if next_ind == rows*cols:
                    return curr_dist + 1
                if visited[next_ind] == 0:
                    visited[next_ind] = 1
                    stack.append([next_ind, curr_dist + 1])

        return -1