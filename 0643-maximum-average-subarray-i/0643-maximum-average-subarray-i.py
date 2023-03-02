class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = float('-inf')
        curr_total = sum(nums[:k-1])
       
        for right in range(k-1,len(nums)):
            curr_total += nums[right]
            max_average = max(max_average,curr_total/k)
            curr_total -= nums[right-k+1]
                
        return max_average
        