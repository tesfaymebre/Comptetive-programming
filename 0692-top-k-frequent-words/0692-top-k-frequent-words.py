class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        freq_key = []
        ans = []
            
        for key,f in freq.items():
            heapq.heappush(freq_key, (-f,key))
                
        for i in range(k):
            ans.append((heapq.heappop(freq_key))[1])
        
        return ans