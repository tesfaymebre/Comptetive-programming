class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # solution 2 using bucket sort
        
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums)
        
        for num, freq in Count.items(): 
            bucket[freq].append(num)
            
        flat_list = [item for sublist in bucket for item in sublist]
        
        return flat_list[-k:]
        
        """
        # solution 1 using heap
        freq = Counter(nums)
        freq_key = []
        
        for key,f in freq.items():
            if len(freq_key) < k:
                heapq.heappush(freq_key, (f,key))
            elif freq_key[0][0] < f:
                heapq.heappushpop(freq_key, (f,key))
        
        return [x[1] for x in freq_key]
        """