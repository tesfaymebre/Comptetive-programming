class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        
        def dp(idx1, mask):
            if (idx1, mask) not in memo:
                if idx1 == len(nums1):
                    return 0
                
                xor_sum = float('inf')
                
                for idx2 in range(len(nums2)):
                    if (mask >> idx2) & 1 == 0:
                        xor_sum = min(xor_sum, (nums1[idx1] ^ nums2[idx2]) + dp(idx1 + 1, mask | (1 << idx2)))
                        
                memo[(idx1, mask)] = xor_sum
                
            return memo[(idx1, mask)]
        
        return dp(0, 0)