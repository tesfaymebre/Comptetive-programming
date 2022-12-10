class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        
        result = []
        
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
                
            left = i+1
            right = n-1
            
            while left < right:
                three_sum = nums[i]+nums[left]+nums[right]
                
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    
                    left += 1
                    
                    while left < n and nums[left-1] == nums[left]:
                        left += 1
                        
        return result
                    