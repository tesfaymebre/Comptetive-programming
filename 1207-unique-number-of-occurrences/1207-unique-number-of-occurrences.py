class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        seen = set()
        
        for key,val in freq.items():
            if val in seen:
                return False
            
            seen.add(val)
            
        return True
        
        