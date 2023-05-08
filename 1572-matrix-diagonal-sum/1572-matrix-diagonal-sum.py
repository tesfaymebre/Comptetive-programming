class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat)
        total = 0
        i,j = 0,0
        
        while i < size:
            total += mat[i][j]
            i += 1
            j += 1
            
        i,j = 0,size-1
        print(total)
        while i < size:
            total += mat[i][j]
            i += 1
            j -= 1
        
        if size&1:
            total -= mat[size//2][size//2]
        
        return total