class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []

        for word in words:
            curr_total = 0

            for c in word:
                curr_total += weights[(ord(c) - ord('a'))]

            curr_total = 25 - (curr_total % 26)
            ans.append(chr(ord('a') + curr_total))

        return "".join(ans)