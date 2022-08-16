class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = dict()
        seen[0] = -1
        summ = 0
        max_len = 0
        
        for i in range(len(nums)):
            summ = (summ + nums[i]) if nums[i] else summ - 1
            
            if summ in seen:
                max_len = max(max_len,i - seen[summ])
            else:
                seen[summ] = i
        
        return max_len