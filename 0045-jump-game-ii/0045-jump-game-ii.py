class Solution:
    def jump(self, nums: List[int]) -> int:
        num_jumps = 0
        indx = 0
        max_indx = nums[0]
        
        for i,val in enumerate(nums[:len(nums)-1]):
            max_indx = max(max_indx,i+val)
            
            if indx == i:
                num_jumps += 1
                indx = max_indx
            
        return num_jumps
        