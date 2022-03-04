class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        freq_key = []
        ans = []
        
        for key,f in freq.items():
            if len(freq_key) < k:
                heapq.heappush(freq_key, (f,key))
            elif freq_key[0][0] < f:
                heapq.heappop(freq_key)
                heapq.heappush(freq_key, (f,key))
                
        for x in freq_key:
            ans.append(x[1])
        
        return ans
        