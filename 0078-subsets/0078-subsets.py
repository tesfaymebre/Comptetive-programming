class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
    