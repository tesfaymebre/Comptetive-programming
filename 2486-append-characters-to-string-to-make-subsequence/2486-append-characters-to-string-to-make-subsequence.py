class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left = 0
        for right in range(len(s)):
            if left == len(t):
                break
                
            if s[right] == t[left]:
                left += 1
                
        return len(t) - left