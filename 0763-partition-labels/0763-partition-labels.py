class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        
        for index,c in enumerate(s):
            last_index[c] = index
         
        arr = []
        left = 0
        right = 0
        
        for curr_idx,c in enumerate(s):
            right = max(right,last_index[c])
            
            if curr_idx == right:
                arr.append(right - left + 1)
                left = right + 1
                
        return arr