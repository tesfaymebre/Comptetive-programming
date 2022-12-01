class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        size = len(s)
        count_1 = Counter(s[:size//2])
        count_2 = Counter(s[size//2:])
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        vowels_1 = 0
        vowels_2 = 0
        
        for vowel in vowels:
            vowels_1 += count_1[vowel]
            vowels_2 += count_2[vowel]
    
        return vowels_1 == vowels_2