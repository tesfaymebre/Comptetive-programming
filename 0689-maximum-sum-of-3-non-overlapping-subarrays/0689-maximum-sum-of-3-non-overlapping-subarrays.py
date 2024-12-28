class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        memo = {}

        def window_sum(nums, k, idx, used, memo):
            if used == 3:
                return 0, []

            if idx - (used * k) > (len(nums)):
                return 0, []

            if (idx, used) in memo:
                return memo[(idx, used)]

            take_curr_sum, take_curr_indices = window_sum(nums, k, idx + k, used + 1, memo)
            take_curr_sum += sum(nums[idx:idx + k])

            skip_curr_sum, skip_curr_indices = window_sum(nums, k, idx + 1, used, memo)

            if take_curr_sum >= skip_curr_sum:
                memo[(idx, used)] = (take_curr_sum, ([idx] + take_curr_indices))
                return memo[(idx, used)]
            else:
                memo[(idx, used)] = (skip_curr_sum, skip_curr_indices)
                return memo[(idx, used)]

        res = window_sum(nums, k, 0, 0, memo)
        return res[1]

        