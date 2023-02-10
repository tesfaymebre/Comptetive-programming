class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        
        mid = len(merged)//2
        
        if len(merged)&1:
            return merged[mid]
        else:
            return (merged[mid-1] + merged[mid])/2