class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        left = 0
        freq = defaultdict(int)

        for right in range(n):
            freq[s[right]] += 1

            while len(freq) == 3:
                count += n - right
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1
  
        return count