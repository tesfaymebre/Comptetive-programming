class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
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
        