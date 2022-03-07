class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        
        for weight in stones:
            heappush(max_heap, -weight)
        
        while len(max_heap) > 1:
            
            temp = -max_heap[0]
            heappop(max_heap)
            heapreplace(max_heap,-abs(temp + max_heap[0]))
        
        return -max_heap[0]