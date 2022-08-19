class Solution:
    def longestPalindrome(self, s: str) -> str:
        in_bound = lambda x: 0 <= x < len(s)
        ans = ''
        
        def center(left,right):
            while in_bound(left) and in_bound(right) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return (left,right)
        
        for i in range(len(s)):
            left,right = center(i-1,i+1)
            subStr = s[left+1:right]
            
            ans = subStr if len(subStr) > len(ans) else ans
            
            left,right = center(i,i+1)
            subStr = s[left+1:right]

            ans = subStr if len(subStr) > len(ans) else ans
            
        return ans
        