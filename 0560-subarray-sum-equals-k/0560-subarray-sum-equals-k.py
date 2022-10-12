class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}

        curSum, ans = 0, 0
        for num in nums:
            curSum += num

            if curSum-k in  prefix:
                ans +=prefix[curSum-k]

            prefix[curSum]= prefix.get(curSum, 0)+1

        return ans