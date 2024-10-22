class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        pattern = 0
        k = len(needle) - 1

        for c in needle:
            idx = ord(c) - ord('a') + 1
            pattern += idx * pow(26,k)
            k -= 1

        window_hash = 0
        k = len(needle) - 1

        for i in range(len(needle)):
            idx = ord(haystack[i]) - ord('a') + 1
            window_hash += idx * pow(26,k)
            k -= 1

        if window_hash == pattern:
            return 0

        left = 0
        right = len(needle)
        k = len(needle) - 1
        while right < len(haystack):
            idx = ord(haystack[left]) - ord('a') + 1
            window_hash -= idx * pow(26,k)

            idx = ord(haystack[right]) - ord('a') + 1
            window_hash *= 26
            window_hash += idx

            if window_hash == pattern:
                return left + 1

            left += 1
            right += 1

        return -1
        