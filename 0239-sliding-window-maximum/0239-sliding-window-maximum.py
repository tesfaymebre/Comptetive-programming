class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        left = 0
        right = 0
        in_bound = lambda index: left <= index <= right 
        max_sliding_window = []
        
        while right < k:
            heapq.heappush(heap,(-nums[right],right))
            right += 1
            
        max_sliding_window.append(-heap[0][0])
        
        while right < len(nums):
            left += 1
            heapq.heappush(heap,(-nums[right],right))
            
            while heap and not in_bound(heap[0][1]):
                heapq.heappop(heap)
                
            max_sliding_window.append(-heap[0][0])
            right += 1
            
        return max_sliding_window
        