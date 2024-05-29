class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        # solution 2 bottom up dp
        size = len(nums1)
        
        dp = [[float('inf')]*(1 << size) for _ in range(size)]
        dp.append([0]*(1 << size))
        
        for idx1 in range(size - 1, -1, -1):
            for mask in range((1 << size) - 1, -1 , -1):
                xor_sum = float('inf')
                
                for idx2 in range(size):
                    if (mask >> idx2) & 1 == 0:
                        xor_sum = min(xor_sum, (nums1[idx1] ^ nums2[idx2]) + dp[idx1 + 1][mask | (1 << idx2)])
                        
                dp[idx1][mask] = xor_sum
                
        return dp[0][0]
        
        """
        # solution 1 top down dp
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
        """