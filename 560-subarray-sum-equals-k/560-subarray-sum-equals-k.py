class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = dict()
        seen[0] = 1
        total = 0
        count = 0
        
        #using prefix sum
        
        for val in nums:
            total += val
            count += seen.get(total - k, 0)
            seen[total] = seen.get(total,0) + 1
            
        return count