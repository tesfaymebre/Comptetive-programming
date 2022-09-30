class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left,right = 0,len(nums)-1
        ptr = 0

        while ptr <= right and left < right:
            if ptr < left:
                ptr += 1
                continue
                
            if nums[left]  == 0:
                left += 1
                continue

            if nums[right] == 2:
                right -= 1
                continue
            
            if nums[ptr] == 0:
                nums[ptr],nums[left] = nums[left],nums[ptr]
                print(1,nums)
            elif nums[ptr] == 2:
                nums[ptr],nums[right] = nums[right],nums[ptr]
                print(2,nums)
            else:
                print(3,nums)
                ptr += 1
        