class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        freq = Counter(s)

        for c in ['a','b','c']:
            if freq[c] < k:
                return -1


        n = len(s)
        right = 0

        while right < n and freq[s[right]] > k:
                freq[s[right]] -= 1
                right += 1

        mini = n - right 
        for left in range(n):
            freq[s[left]] += 1

            while right < n and freq[s[right]] > k:
                freq[s[right]] -= 1
                right += 1

            mini = min(mini, (n - right) + left + 1)

        return mini
