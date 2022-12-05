class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #bottom up dp solution
        size = len(s)
        dp = [[] for _ in range(size+1)]
        dp[size] = [[]]
        
        for left in range(size-1,-1,-1):
            result = []
            
            for right in range(left,size):
                if s[left:right+1] == s[left:right+1][::-1]:
                    sub_partitions = dp[right+1]
                    
                    result += [[s[left:right+1]] + p for p in sub_partitions]
                    
            dp[left] = result[:]
            
        return dp[0]
        
        """
        #top down dp solution
        
        def helper(left):
            if left not in memo:
                if left == len(s):
                    return [[]]

                result = []

                for right in range(left,len(s)):
                    if s[left:right+1] == s[left:right+1][::-1]:
                        sub_partitions = helper(right+1)

                        result += [[s[left:right+1]] + p for p in sub_partitions]

                memo[left] = result
            
            return memo[left]
        
        memo = {}
        
        return helper(0)
        """