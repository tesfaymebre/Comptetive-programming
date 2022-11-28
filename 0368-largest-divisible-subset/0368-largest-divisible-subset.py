class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        seen = {}
        
        def helper(idx,path):
            if len(self.res) < len(path):
                self.res = path[:]
            
            for i in range(idx+1,len(nums)):
                if nums[i] % nums[idx] == 0:
                    if nums[i] not in seen or seen[nums[i]] < len(path):
                        seen[nums[i]] = len(path)
                        helper(i,path + [nums[i]])
                    
            return
        
        nums.sort()
        self.res = []
        
        for i in range(len(nums)):
            helper(i,[nums[i]])
       
        return self.res
            