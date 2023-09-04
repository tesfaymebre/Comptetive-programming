class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        longest = 0
        
        memo = defaultdict(int)
       
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i]-nums[j]
                memo[(i,diff)] = 1 + memo[(j,diff)]
                longest = max(longest,memo[(i,diff)])
                
        return longest + 1