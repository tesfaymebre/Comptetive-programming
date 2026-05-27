class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_idx_lower = [-1] * 26
        first_idx_upper = [-1] * 26

        for i, c in enumerate(word):
            if c.islower():
                last_idx_lower[ord(c) - ord('a')] = i
            elif first_idx_upper[ord(c) - ord('A')] == -1:
                first_idx_upper[ord(c) - ord('A')] = i

        count = 0
        print(last_idx_lower, first_idx_upper)
        for j in range(26):
            if last_idx_lower[j] != -1 and first_idx_upper[j] != -1:
                count += last_idx_lower[j] < first_idx_upper[j]

        return count

        