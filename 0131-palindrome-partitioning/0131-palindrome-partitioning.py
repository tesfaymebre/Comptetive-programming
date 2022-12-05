class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
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