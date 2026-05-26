class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        freq = Counter(word)
        count = 0

        for key in freq:
            if key.islower() and key.upper() in freq:
                count += 1

        return count

        