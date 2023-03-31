class Solution:
    def __init__(self):
        self.count = 0
        
    def countPairs(self,left_half,right_half,diff):
        size1 = len(left_half)
        size2 = len(right_half)
        p1 = 0
        p2 = 0
        
        while p1 < size1 and p2 < size2:
            if left_half[p1] <= right_half[p2] + diff:
                self.count += size2 - p2
                p1 += 1
            else:
                p2 += 1
                
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
    
    def merge_sort(self,left,right,nums,diff):
        if left == right:
            return [nums[left]]
        
        mid = left + (right-left)//2
        left_half = self.merge_sort(left,mid,nums,diff)
        right_half = self.merge_sort(mid+1,right,nums,diff)
        
        self.countPairs(left_half,right_half,diff)
        return self.merge(left_half,right_half)
    
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        new_nums = [x-y for x,y in zip(nums1,nums2)]
        
        self.merge_sort(0,len(new_nums)-1,new_nums,diff)
        return self.count
        