class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        memo = {}

        def dp(prev,curr):
            if (prev,curr) not in memo:
                if curr == len(words):
                    return []

                not_pick = dp(prev, curr + 1)
                pick = []

                if groups[prev] != groups[curr] and len(words[prev]) == len(words[curr]):
                    hamming_dist = 0
                    for i in range(min(len(words[prev]),len(words[curr]))):
                        hamming_dist += words[prev][i] != words[curr][i]

                    if hamming_dist == 1:
                        pick.append(words[curr])
                        pick.extend(dp(curr,curr+1))

                if len(pick) > len(not_pick):
                    memo[(prev,curr)] = pick
                else:
                    memo[(prev,curr)] = not_pick

            return memo[(prev,curr)]

        max_subsequence = []
        for i in range(len(words)):
            temp = [words[i]] + dp(i,i+1)
            if len(max_subsequence) < len(temp):
                max_subsequence = temp

        return max_subsequence
        