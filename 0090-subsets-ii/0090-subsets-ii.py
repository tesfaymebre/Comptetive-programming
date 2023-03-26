class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        
        def backT(idx,path):
            if idx >= len(nums):
                temp = tuple(path)
                
                if temp not in seen:
                    ans.append(path[:])
                    seen.add(temp)
                    
                return
            
            for i in range(idx,len(nums)):
                backT(i+1,path + [nums[i]])
                
            temp = tuple(path)
            if temp not in seen:
                ans.append(path[:])
                seen.add(temp)
        
        nums.sort()
        backT(0,[])
        return ans