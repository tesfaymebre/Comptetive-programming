class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        
        while i < len(nums) and k > 0:
            if nums[i] < 0:
                nums[i] = -1*nums[i]
                k -= 1
            else:
                break
                
            i += 1
        
        nums.sort()
        
        if k % 2 == 1:
            nums[0] = -1*nums[0]
        
        return sum(nums)