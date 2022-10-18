class Solution:
    def fill_right(self,start_state,matrix):
        curr_value = start_state[2]
        n = len(matrix)
        
        for i in range(start_state[1], n):
            curr_value += 1
            if matrix[start_state[0]][i] == 0:
                matrix[start_state[0]][i] = curr_value
                start_state[1] += 1
            else:
                break
                
            start_state[2] = curr_value
        
        start_state[0] += 1
        start_state[1] -= 1
            
    def fill_down(self,start_state,matrix):
        n = len(matrix)
        curr_value = start_state[2]
        
        for i in range(start_state[0],n):
            curr_value += 1
            print(start_state)
            if matrix[i][start_state[1]] == 0:
                matrix[i][start_state[1]] = curr_value
                start_state[0] += 1
            else:
                break
                
            start_state[2] = curr_value 
        
        start_state[0] -= 1
        start_state[1] -= 1
        
    def fill_left(self,start_state,matrix):
        n = len(matrix)
        curr_value = start_state[2]
        
        for i in range(start_state[1],-1,-1):
            curr_value += 1
            if matrix[start_state[0]][i] == 0:
                matrix[start_state[0]][i] = curr_value
                start_state[1] -= 1
            else:
                break
                
            start_state[2] = curr_value
        
        start_state[0] -= 1
        start_state[1] += 1
            
    def fill_up(self,start_state,matrix):
        n = len(matrix)
        curr_value = start_state[2]
        
        for i in range(start_state[0],-1,-1):
            curr_value += 1
            if matrix[i][start_state[1]] == 0:
                matrix[i][start_state[1]] = curr_value
                start_state[0] -= 1
            else:
                break
                
            start_state[2] = curr_value 
        
        start_state[0] += 1
        start_state[1] += 1
        
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        start_state = [0,0,0]
        for _ in range(n):
            self.fill_right(start_state,matrix)
            self.fill_down(start_state,matrix)
            self.fill_left(start_state,matrix)
            self.fill_up(start_state,matrix)  
        return matrix