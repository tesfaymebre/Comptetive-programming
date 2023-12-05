class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        count = 0
        
        for key,val in freq.items():
            count += val * ( val - 1) // 2  
            
        return count