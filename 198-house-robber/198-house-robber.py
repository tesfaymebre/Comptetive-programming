class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        
        for x in nums:
            temp = prev
            prev = curr
            curr = max(temp + x, curr)
            
        return curr