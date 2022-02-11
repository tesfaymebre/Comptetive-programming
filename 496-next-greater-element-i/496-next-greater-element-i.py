class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                dic[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        for j in range(len(nums1)):
            nums1[j] = dic.get(nums1[j],-1)
        
        return nums1
        