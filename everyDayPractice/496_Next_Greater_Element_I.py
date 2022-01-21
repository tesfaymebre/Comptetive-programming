class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums1)):
            max = -1
            for j in range(len(nums2)-1,-1,-1):
                if nums1[i] < nums2[j]:
                    max = nums2[j]
                elif nums1[i] == nums2[j]:
                    ans.append(max)
                    break
        return ans
