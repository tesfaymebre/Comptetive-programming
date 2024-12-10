class Solution:
    def maximumLength(self, s: str) -> int:
        def checker(window):
            freq = defaultdict(int)

            for i in range(len(s)-window + 1):
                temp = s[i:i+window]
                if len(set(temp)) == 1:
                    freq[temp] += 1

                    if freq[temp] == 3:
                        return True

            return False

        left = 1
        right = len(s)
        best = -1

        while left <= right:
            mid = left + (right - left)//2

            if checker(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1

        return best