class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        
        for idx,num in enumerate(nums):
            arr.append((num,idx))
        
        arr.sort()
        
        right = len(arr)-1
        
        for left in range(len(arr)):
            while right > left and arr[left][0] + arr[right][0] > target:
                right -= 1
                
            if arr[left][0] + arr[right][0] == target:
                return [arr[left][1],arr[right][1]]