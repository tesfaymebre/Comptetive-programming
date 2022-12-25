class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer_nums1 = m-1
        pointer_nums2 = n-1
        
        for i in range(len(nums1)-1,-1,-1):
            if pointer_nums2 < 0:
                break
                
            if pointer_nums1 < 0 or nums2[pointer_nums2] > nums1[pointer_nums1]:
                nums1[i] = nums2[pointer_nums2]
                pointer_nums2 -= 1
            else:
                nums1[i] = nums1[pointer_nums1]
                pointer_nums1 -= 1