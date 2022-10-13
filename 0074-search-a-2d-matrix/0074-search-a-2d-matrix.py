class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def BS(row,target):
            l,r = 0,len(row)-1
            
            while l <= r:
                mid = l + (r-l)//2
                
                if row[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return l
        
        for row in matrix:
            if row[BS(row,target)-1] == target:
                return True
            
        return False
            