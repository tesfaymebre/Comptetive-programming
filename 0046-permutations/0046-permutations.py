class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        def backT(seen,path):
            if len(path) == len(nums):
                self.res.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    backT(seen,path + [nums[i]])
                    seen.remove(nums[i])
                    
            return
        
        backT(set(),[])
        return self.res