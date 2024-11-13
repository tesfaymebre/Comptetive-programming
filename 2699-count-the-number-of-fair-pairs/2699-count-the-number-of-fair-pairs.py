class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def bisect_left(left,right,target):
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        res = 0
        l = 0
        r = len(nums) - 1

        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum > upper:
                r -= 1
            elif curr_sum < lower:
                l += 1
            else:
                res += r - bisect_left(l+1,r,lower - nums[l]) + 1
                l += 1

        return res