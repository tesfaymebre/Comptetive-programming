class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count = 0

        for i in range(len(nums)):
            curr = 0

            for j in range(i,len(nums)):
                curr += 1 if nums[j] == target else -1
                count += 1 if curr > 0 else 0
                
        return count