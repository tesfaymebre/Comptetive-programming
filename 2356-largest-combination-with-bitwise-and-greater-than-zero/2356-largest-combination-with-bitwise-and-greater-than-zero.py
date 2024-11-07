class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        maxi = 0

        for i in range(32):
            curr_count = 0

            for num in candidates:
                curr_count += (num >> i) & 1

            maxi = max(maxi,curr_count)

        return maxi