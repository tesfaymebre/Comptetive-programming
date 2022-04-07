class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        for i in range(len(palindrome)):
            if ord(palindrome[i]) > 97:
                if len(palindrome) % 2 == 1 and i == len(palindrome)// 2:
                    continue
                return palindrome[:i] + "a" + palindrome[i + 1:]
        
        return palindrome[:len(palindrome)-1] + "b"