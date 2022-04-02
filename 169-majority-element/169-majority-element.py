class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurance = Counter(nums)
        return max(occurance, key = occurance.get)