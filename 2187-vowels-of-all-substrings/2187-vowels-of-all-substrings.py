class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        count = 0
        vowels = {'a','e','i','o','u'}

        for i in range(n):
            if word[i] in vowels:
                count += (i+1) * (n-i)

        return count