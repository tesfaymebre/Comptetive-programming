class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - right)//2
    
            if n - mid <= citations[mid]:
                right = mid - 1
            else:
                left = mid + 1  
                
        return n - left