class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        freq['l'] //= 2
        freq['o'] //= 2
        mini = float('inf')

        for c in "balloon":
            mini = min(mini, freq[c])

        return mini