class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left_side = []
        right_side = []
        count = 0
        
        for i in range(len(nums)):
            if nums[i] < pivot:
                left_side.append(nums[i])
            elif nums[i] > pivot:
                right_side.append(nums[i])
            else:
                count += 1
        
        return left_side + [pivot]*count + right_side