class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete_col = 0
        
        for col in range(len(strs[0])):
            for row in range(1,len(strs)):
                if strs[row-1][col] > strs[row][col]:
                    delete_col += 1
                    break
                    
        return delete_col