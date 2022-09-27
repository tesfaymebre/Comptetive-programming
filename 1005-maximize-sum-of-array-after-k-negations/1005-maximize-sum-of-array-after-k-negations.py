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
        
        return sum(nums) - 2*min(nums) if k % 2 else sum(nums)