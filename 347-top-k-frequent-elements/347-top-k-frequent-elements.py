class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        freq_key = []
        
        for key,f in freq.items():
            if len(freq_key) < k:
                heapq.heappush(freq_key, (f,key))
            elif freq_key[0][0] < f:
                heapq.heappushpop(freq_key, (f,key))
        
        return [x[1] for x in freq_key]
        