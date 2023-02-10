class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findMedian(arr1, arr2, mid):
            if not arr1:
                return arr2[mid]
            
            if not arr2:
                return arr1[mid]
            
            median_idx1, median_idx2 = len(arr1) // 2 , len(arr2) // 2
            median_val1, median_val2 = arr1[median_idx1], arr2[median_idx2]

            if median_idx1 + median_idx2 < mid:
                
                if median_val1 > median_val2:
                    return findMedian(arr1, arr2[median_idx2 + 1:], mid - median_idx2 - 1)
                else:
                    return findMedian(arr1[median_idx1 + 1:], arr2, mid - median_idx1 - 1)
            else:
                if median_val1 > median_val2:
                    return findMedian(arr1[:median_idx1], arr2, mid)
                else:
                    return findMedian(arr1, arr2[:median_idx2], mid)
            
        total_size = len(nums1) + len(nums2)
        
        if total_size&1:
            return findMedian(nums1, nums2, total_size // 2)
        else:
            return (findMedian(nums1,nums2,total_size // 2) + findMedian(nums1,nums2,total_size // 2 - 1)) / 2.   

    