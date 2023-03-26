class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        seen = set()
        
        def backT(visited,path):
            if len(path) == len(nums):
                temp = tuple(path)
                
                if temp not in seen:
                    self.res.append(path[:])
                    seen.add(temp)
                    
                return
            
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    backT(visited,path + [nums[i]])
                    visited.remove(i)
                    
            return
        
        backT(set(),[])
        return self.res
            
        