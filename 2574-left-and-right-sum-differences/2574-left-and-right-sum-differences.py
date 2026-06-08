class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        total = sum(nums)
        running_sum = 0

        for num in nums:
            answer.append(abs(2*running_sum - total + num))
            running_sum += num

        return answer
