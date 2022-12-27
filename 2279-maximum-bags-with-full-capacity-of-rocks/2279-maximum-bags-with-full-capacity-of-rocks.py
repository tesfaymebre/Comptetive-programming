class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        size = len(capacity)
        
        additional_need = []
        
        for i in range(size):
            additional_need.append(capacity[i]-rocks[i])
            
        additional_need.sort()
        
        for j in range(size):
            if additional_need[j] > additionalRocks:
                return j
            
            additionalRocks -= additional_need[j]
            
        return size