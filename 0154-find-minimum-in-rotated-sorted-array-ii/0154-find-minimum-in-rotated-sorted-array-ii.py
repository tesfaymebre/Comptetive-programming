class Solution:
    def findMin(self, nums: List[int]) -> int:
        best = nums[0]
        left = 0
        right = len(nums) - 1

        while right > 0 and nums[right] == nums[right-1]:
            right -= 1

        while (left <= right):
            mid = left + (right - left) // 2
           
            if nums[left] <= nums[mid]:
                best = min(best, nums[left])
                left = mid + 1
            else:
                best = min(best, nums[mid])
                right = mid - 1
        
        return best


        