class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mods = [1] + [0] * k

        ret = 0
        curr = 0
        for num in nums:
            curr = (curr + num) % k

            ret += mods[curr]

            mods[curr] += 1

        return ret