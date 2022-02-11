class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        max_h_indx = 0
        
        for indx,val in enumerate(citations):
            if indx + 1 < val:
                max_h_indx = max(max_h_indx,indx+1)
            else:
                max_h_indx = max(max_h_indx, val)
                
        return max_h_indx
                