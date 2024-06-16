class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch_needed = 0
        missed = 1
        index = 0
        
        while missed <= n:
            if index < len(nums) and nums[index] <= missed:
                missed += nums[index]
                index += 1
            else:
                missed += missed
                patch_needed += 1
                
        return patch_needed