class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        maxx = 0
        
        if k == 0:
            curr = 0
            for i in range(len(nums)):
                if nums[i]== 1:
                    curr += 1
                else:
                    maxx = max(maxx,curr)
                    curr = 0
                    
            return max(maxx,curr)
        
        while left <= right and right < len(nums):
            if nums[right] == 1:
                right += 1
            elif k > 0:
                k -= 1
                right += 1
            elif nums[left] == 0:
                maxx = max(maxx,right - left)
                k += 1
                left += 1
            else:
                maxx = max(maxx,right - left)
                left += 1
                                  
        return max(maxx,right - left)