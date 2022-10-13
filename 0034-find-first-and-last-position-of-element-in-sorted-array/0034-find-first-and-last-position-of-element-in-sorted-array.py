class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def BST_left(arr,t):
            left,right = 0,len(arr) - 1
            while left <= right:
                mid = left + (right - left)//2
                if arr[mid] < target: left = mid + 1
                else: right = mid - 1      
            return left
        
        def BST_right(arr,t):
            left,right = 0,len(arr)-1
            while left <= right:
                mid = left + (right - left)//2
                if arr[mid] > target: right = mid - 1
                else: left = mid + 1   
            return left
                
        left,right = BST_left(nums,target),BST_right(nums,target)-1
        return [left,right] if left <= right else [-1,-1]