class Solution:
    def isGood(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        for i in range(1, len(nums)-1):
            if freq[i]!= 1:
                return False

        return freq[len(nums)-1] == 2
