class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        curr_sum = 0

        for i in range(k - 1):
            curr_sum += nums[i]
            freq[nums[i]] += 1

        maxi = 0

        left = 0
        for right in range(k - 1, len(nums)):
            curr_sum += nums[right]
            freq[nums[right]] += 1

            if len(freq) == k:
                maxi = max(maxi,curr_sum)

            curr_sum -= nums[left]
            freq[nums[left]] -= 1

            if freq[nums[left]] == 0:
                del freq[nums[left]]

            left += 1

        return maxi