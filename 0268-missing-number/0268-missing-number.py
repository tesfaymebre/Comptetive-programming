class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #solution using cyclic sort
        missing_num = len(nums)
        
        for i in range(len(nums)):
            while nums[i] < len(nums) and nums[i] != i:
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]
                
            if nums[i] != i:
                missing_num = i
                
        return missing_num
            
        
        """
        #solution using bit manipulation
        
        n = len(nums)
        xor = nums[0] ^ 0 ^ n
        
        for i in range(1, n):
            xor = xor ^ nums[i] ^ i
        
        return xor
        """