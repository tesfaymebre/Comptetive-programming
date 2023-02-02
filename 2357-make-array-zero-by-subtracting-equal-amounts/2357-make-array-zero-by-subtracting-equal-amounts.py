class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        subtracted = 0
        operation = 0
        
        for num in nums:
            if num - subtracted > 0:
                subtracted += num - subtracted
                operation += 1
                
        return operation