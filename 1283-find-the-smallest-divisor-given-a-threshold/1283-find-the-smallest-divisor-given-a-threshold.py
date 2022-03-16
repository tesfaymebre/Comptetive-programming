class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        ans = right
        summ = 0
        while left <= right:
            mid = left + (right - left)//2
            
            for x in nums:
                summ += ceil(x / mid)
            
            if summ <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
            
            summ = 0
        return ans
                