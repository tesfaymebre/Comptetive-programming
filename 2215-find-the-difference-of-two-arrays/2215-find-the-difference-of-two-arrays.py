class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        uniq1 = set(nums1)
        uniq2 = set(nums2)
        
        answer = [[],[]]
        
        for num in uniq1:
            if num not in uniq2:
                answer[0].append(num)
                
        for num in uniq2:
            if num not in uniq1:
                answer[1].append(num)
                
        return answer
        