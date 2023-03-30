class Solution:
    def merge(self,left_half,right_half):
        arr = []
        p1 = 0
        p2 = 0
        
        while p1 < len(left_half) and p2 < len(right_half):
            if left_half[p1] <= right_half[p2]:
                arr.append(left_half[p1])
                p1 += 1
            else:
                arr.append(right_half[p2])
                p2 += 1
                
        arr += left_half[p1:] + right_half[p2:]
        return arr
    
    def merge_sort(self,left,right,nums):
        if left == right:
            return [nums[left]]
        
        mid = left + (right-left)//2
        left_half = self.merge_sort(left,mid,nums)
        right_half = self.merge_sort(mid+1,right,nums)
        
        return self.merge(left_half,right_half)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(0,len(nums)-1,nums)    