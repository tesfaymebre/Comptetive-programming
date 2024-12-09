class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix_sum = [1]

        for i in range(1,len(nums)):
            if (nums[i] & 1 and not nums[i-1] & 1) or (not nums[i] & 1 and nums[i-1] & 1):
                prefix_sum.append(prefix_sum[-1] + 1)
            else:
                prefix_sum.append(1)

        answer = []

        for fro,to in queries:
            if (prefix_sum[to] - prefix_sum[fro])  == (to - fro):
                answer.append(True)
            else:
                answer.append(False)

        return answer
        