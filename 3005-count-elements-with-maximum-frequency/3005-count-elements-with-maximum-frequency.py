class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        
        total_freq = 0
        
        for key,val in freq.items():
            if val == max_freq:
                total_freq += max_freq
                
        return total_freq