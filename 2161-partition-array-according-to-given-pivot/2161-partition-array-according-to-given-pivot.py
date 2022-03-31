class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            if nums[i] < pivot:
                ans.append(nums[i])
        
        for j in range(len(nums)):
            if nums[j] == pivot:
                ans.append(nums[j])
        
        for k in range(len(nums)):
            if nums[k] > pivot:
                ans.append(nums[k])
        return ans