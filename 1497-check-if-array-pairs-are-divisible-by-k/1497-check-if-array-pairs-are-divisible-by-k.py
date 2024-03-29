class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = defaultdict(int)
        
        for num in arr:
            temp = (- num) % k
            
            if temp in freq:
                freq[temp] -= 1
                
                if freq[temp] == 0:
                    del freq[temp]
            else:
                freq[num % k] += 1
                
        return not freq