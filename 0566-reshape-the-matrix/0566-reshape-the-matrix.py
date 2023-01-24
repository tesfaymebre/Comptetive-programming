class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m*n != r*c:
            return mat
        
        new_mat = []
        
        for i in range(r):
            temp = []
            
            for j in range(c):
                uniq_number = i*c + j
                curr_row = uniq_number // n
                curr_col = uniq_number % n
                
                temp.append(mat[curr_row][curr_col])
            
            new_mat.append(temp)
                
        return new_mat