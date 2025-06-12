class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = [1,nums[-1]]

        for i in range(len(nums)-2,-1,-1):
            postfix.append(postfix[-1]*nums[i])

        prefix = 1
        answer = []
        print(postfix)
        for i in range(len(nums)):
            answer.append(prefix * postfix[-(i+2)])
            prefix *= nums[i]

        return answer