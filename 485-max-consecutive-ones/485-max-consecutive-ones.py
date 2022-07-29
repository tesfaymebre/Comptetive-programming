class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        prev = 0
        
        for val in nums:
            if val == 1:
                prev += 1
            else:
                prev = 0
                
            count = max(count,prev)
                
        return count