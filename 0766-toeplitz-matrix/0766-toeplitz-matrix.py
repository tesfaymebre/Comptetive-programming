class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonal = dict()
        
        for i in range(len(matrix)):
            diagonal[i] = matrix[i][0]
            
        for j in range(1,len(matrix[0])):
            diagonal[-j] = matrix[0][j]
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if diagonal[i-j] != matrix[i][j]:
                    return False
                
        return True