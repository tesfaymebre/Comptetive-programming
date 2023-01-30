class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0,1,1] + [None] * 37
        
        def helper(curr):
            if memo[curr] != None:
                return memo[curr]

            memo[curr] = helper(curr-1) + helper(curr-2) + helper(curr-3)
            return memo[curr]
        
        return helper(n)