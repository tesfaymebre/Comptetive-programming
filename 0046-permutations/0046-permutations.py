class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #using bit manipulation 
        n = len(nums)
        self.res = []
        
        def backT(seen,path):
            if len(path) == len(nums):
                self.res.append(path[:])
                return
            
            for i in range(len(nums)):
                if seen & (1<<(n-i-1)) == 0:
                    seen |= 1 << (n-i-1)
                    backT(seen,path + [nums[i]])
                    seen ^= 1 << (n-i-1)
                    
            return
        
        backT(0,[])
        return self.res
    
    """
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
    """