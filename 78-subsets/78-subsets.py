class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nth_bit = 1 << n
        ans = []
        
        for i in range(2**n):
            bit = bin(i | nth_bit)[3:] 
            temp = []
            
            for j in range(n):
                if int(bit[j]):
                    temp.append(nums[j])
            ans.append(temp)
        
        return ans
                
            
            