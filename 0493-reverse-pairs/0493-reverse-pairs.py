class Solution:
    def __init__(self):
        self.count = 0
        
    def countReversePairs(self,left_half,right_half):
        p1 = len(left_half)-1
        p2 = len(right_half)-1
        
        while p1 > -1 and p2 > -1:
            if left_half[p1] > 2*right_half[p2]:
                self.count += p2+1
                p1-=1
            else:
                p2-=1
        return
        
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
    
    def mergeSort(self,left,right,nums):
        if left == right:
            return [nums[left]]
        
        mid = left + (right-left)//2
        left_half = self.mergeSort(left,mid,nums)
        right_half = self.mergeSort(mid+1,right,nums)
        
        self.countReversePairs(left_half,right_half)
        return self.merge(left_half,right_half)
    
    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(0,len(nums)-1,nums)
        return self.count