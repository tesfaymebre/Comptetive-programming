class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        prefix_sum = 0
        count = 0
        
        #using prefix sum
        
        for val in nums:
            prefix_sum += val
            count += d[prefix_sum - k]
            d[prefix_sum] += 1
            
        return count