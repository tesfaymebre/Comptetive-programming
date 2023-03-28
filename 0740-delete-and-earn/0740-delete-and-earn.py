class Solution:
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        arr = sorted(freq.keys())
        n = len(freq)
        memo = {}

        def dp(i):
            if i not in memo:
                if i >= len(arr):
                    return 0
                
                score = 0
                if i+1 < len(arr) and arr[i]+1 == arr[i+1]:
                    score = max(score,arr[i]*freq[arr[i]] + dp(i+2))
                else:
                    score = max(score,arr[i]*freq[arr[i]] + dp(i+1))
                    
                score = max(score,dp(i+1))
                
                memo[i] = score
                
            return memo[i]
        
        return dp(0)
        