class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # solution 1 using heap
        
        min_heap = []
        
        for i in range(len(nums)):
            
            if len(min_heap) < k:
                heappush(min_heap, nums[i])
            elif min_heap[0] < nums[i]:
                heapreplace(min_heap, nums[i])
        
        return min_heap[0]
        