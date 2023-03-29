class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #using cyclic sort
        for i in range(len(nums)):
            while nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
              
        for j,num in enumerate(nums):
            if num != j + 1:
                return num
        
        """
        #using binary search
        
        def check(mid):
            count = 0
            
            for i in nums:
                if i <= mid:
                    count += 1
                    
            return count
            
        left,right = 1,max(nums)
        temp = 0
        
        while left <= right:
            mid = left + (right - left)//2
            count = check(mid)
            
            if count > mid:
                temp = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return temp
        """
        