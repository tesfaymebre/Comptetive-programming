class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        def left_down_diagonal(row,col):
            temp = []
            while inbound(row,col):
                temp.append(mat[row][col])
                row += 1
                col -= 1
                
            if diagonal&1 == 0:
                temp = temp[::-1]
                
            return temp
        
        inbound = lambda r,c: -1 < r < len(mat) and -1 < c < len(mat[0])
        result = []
        diagonal = 0
        
        for i in range(len(mat[0])):
            row = 0
            col = i
        
            result += left_down_diagonal(row,col)
            diagonal += 1
            
        for j in range(1,len(mat)):
            row = j
            col = len(mat[0])-1
            
            result += left_down_diagonal(row,col)
            diagonal += 1
            
        return result
        