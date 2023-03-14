class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #bit manipulation
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
                
        
        """
        #backtrack solution
        
        ans = []
        
        def backT(idx,path):
            if idx >= len(nums):
                ans.append(path)
                return
                
            for i in range(idx,len(nums)):
                backT(i+1,path + [nums[i]])
            
            ans.append(path)
            return
            
        backT(0,[])
        return ans
        """
    