class Solution:
    def maxScore(self, nums: List[int]) -> int:

        def dfs(a, i):
            if (a, i) not in memo:
                n = len(a)
                res = 0
                for j in range(n):
                    for k in range(j+1, n):
                        new_a = a[:j] + a[j+1:k] + a[k+1:]
                        res = max(res, i * gcd(a[j], a[k]) + dfs(new_a, i+1))

                memo[(a, i)] = res
                
            return memo[(a, i)]
        
        nums.sort()
        memo = {}
        return dfs(tuple(nums),1)
        