class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        def dp(p1,p2):
            if (p1,p2) not in memo:
                if p1 >= len(nums1) or p2 >= len(nums2):
                    return 0

                max_lines = 0
                
                if nums1[p1] == nums2[p2]:
                    max_lines = max(max_lines,1+dp(p1+1,p2+1))
                    
                max_lines = max(max_lines,dp(p1+1,p2),dp(p1,p2+1))
                
                memo[(p1,p2)] = max_lines
                
            return memo[(p1,p2)]
        
        memo = {}
        return dp(0,0)