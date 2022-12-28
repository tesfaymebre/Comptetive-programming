class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        max_heap = []
        
        for pile in piles:
            heapq.heappush(max_heap,-1*pile)
            
        while k > 0:
            curr_max_pile = -1*max_heap[0]
            remove_stones = floor(curr_max_pile/2)
            total -= remove_stones
            heapq.heapreplace(max_heap,-(curr_max_pile - remove_stones))
            k -= 1
            
        return total