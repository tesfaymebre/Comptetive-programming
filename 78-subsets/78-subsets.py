class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        for i in range(2**n):
            x = '{0:010b}'. format(i)[::-1]
            temp = []
            
            for j in range(n):
                if int(x[j]):
                    temp.append(nums[j])
            ans.append(temp)
        
        return ans
                
            
            