class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = float('-inf')
        curr_total = 0
        left = 0
        for right in range(len(nums)):
            curr_total += nums[right]
            
            if right - left + 1 == k:
                max_average = max(max_average,curr_total/k)
                curr_total -= nums[left]
                left += 1
                
        return max_average
        