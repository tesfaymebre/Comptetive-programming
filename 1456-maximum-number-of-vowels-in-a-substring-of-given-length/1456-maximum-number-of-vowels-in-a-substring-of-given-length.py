class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        max_num = 0
        count = 0
        
        left = 0
        for right in range(len(s)):
            if s[right] in vowels:
                count += 1
                
            if right - left + 1 == k:
                max_num = max(max_num,count)
                
                if s[left] in vowels:
                    count -= 1
                
                left += 1
                
        return max_num
                