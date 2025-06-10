class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = dict()

        for idx,num in enumerate(nums):
            diff = target - num

            if diff in track:
                return [track[diff],idx]

            track[num] = idx

        return []